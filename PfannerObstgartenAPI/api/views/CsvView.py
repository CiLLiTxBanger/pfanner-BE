# under construction
from rest_framework import permissions
from rest_framework import generics
from rest_framework import permissions
from api.models import LabMeasurement, OrchardMeasurement, Tree
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import csv


class ExportLabMeasurementsCSVByTreeId(APIView):
    def get(self, request, treeId, *args, **kwargs):
        treeId = treeId
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="LabMeasurements_Tree_{}.csv"'.format(str(treeId))

        writer = csv.writer(response)
        labMeasurements = LabMeasurement.objects.filter(tree = treeId)

        #Headlines
        writer.writerow(['sep=,'])
        writer.writerow(['Strength Measurement', 'Flavor Measurement', 'Acid Measurement', 'Sugar Measurement', 'Status', 'Last Modified', 'Created on'])

        #Rows
        for lM in labMeasurements:
            writer.writerow([' '+str(lM.strengthMeasurement), lM.flavorMeasurement, ' '+str(lM.acidMeasurement), ' '+str(lM.sugarMeasurement), lM.status, lM.timestamp.strftime("%d.%m.%Y - %H:%M"), lM.created_on.strftime("%d.%m.%Y - %H:%M")])

        return response

class ExportOrchardMeasurementsCSVByTreeId(APIView):
    def get(self, request, treeId, *args, **kwargs):
        treeId = treeId
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="OrchardMeasurements_Tree_{}.csv"'.format(str(treeId))

        writer = csv.writer(response)
        orchardMeasurements = OrchardMeasurement.objects.filter(tree = treeId)

        #Headlines
        writer.writerow(['sep=,'])
        writer.writerow(['Tree ID', 'Variety Name', 'Frost Sensitivity', 'Growth Habit', 'Yield Habit', 'Season', 'Temperature', 'Precipitation', 'Late Frost', 'Status', 'Created on'])

        #Rows
        for oM in orchardMeasurements:
            writer.writerow([oM.tree, oM.tree__variety__name, oM.frostSensitivity, oM.growthHabit, oM.yieldHabit, oM.season, oM.temperature, oM.precipitation, oM.lateFrost, oM.status, oM.created_on.strftime("%d.%m.%Y - %H:%M")])

        return response
