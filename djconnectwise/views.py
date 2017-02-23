# -*- coding: utf-8 -*-
import json
import logging

from braces import views
from djconnectwise.sync import TicketSynchronizer

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.generic import View

from .models import Ticket


logger = logging.getLogger(__name__)


class ConnectWiseCallBackView(views.CsrfExemptMixin,
                              views.JsonRequestResponseMixin, View):
    def __init__(self, *args, **kwargs):
        super(ConnectWiseCallBackView, self).__init__(*args, **kwargs)
        self.synchronizer = TicketSynchronizer()


class TicketCallBackView(ConnectWiseCallBackView):

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode(encoding='utf-8'))
        action = request.GET.get('action')

        if action is None:
            msg = 'Received ticket callback with no action parameter.'
            logger.warning(msg)

            err = "The 'action' parameter is required."
            return HttpResponseBadRequest(err)
        ticket_id = request.GET.get('id')

        if ticket_id is None:
            msg = 'Received ticket callback with no ticket_id parameter.'
            logger.warning(msg)

            err = "The 'ticket_id' parameter is required."
            return HttpResponseBadRequest(err)

        logger.debug('{} {}: {}'.format(action.upper(), ticket_id, body))

        if action == 'deleted':
            logger.info('Ticket Deleted CallBack: {}'.format(ticket_id))
            Ticket.objects.filter(id=ticket_id).delete()
        else:
            logger.info('Ticket Pre-Update: {}'.format(ticket_id))
            ticket = self.synchronizer \
                .service_client \
                .get_ticket(ticket_id)

            if ticket:
                logger.info('Ticket Updated CallBack: {}'.format(ticket_id))
                self.synchronizer.sync_ticket(ticket)

        # we need not return anything to connectwise
        return HttpResponse(status=204)
