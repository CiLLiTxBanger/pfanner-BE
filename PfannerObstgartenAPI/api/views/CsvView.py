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
import codecs


class ExportLabMeasurementsCSVByTreeId(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, treeId, *args, **kwargs):
        treeId = treeId
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="LabMeasurements_Tree_{}.csv"'.format(str(treeId))
        response.write(codecs.BOM_UTF8)

        writer = csv.writer(response, delimiter= ';', dialect = 'excel')
        labMeasurements = LabMeasurement.objects.filter(tree = treeId)

        #Headlines
        writer.writerow(['Tree ID', 'Variety Name', 'Strength Measurement', 'Flavor Measurement', 'Acid Measurement', 'Sugar Measurement', 'Status', 'Last Modified', 'Created on'])

        #Rows
        for lM in labMeasurements:
            writer.writerow([lM.tree.id, lM.tree.variety.name, ' '+str(lM.strengthMeasurement), lM.flavorMeasurement, ' '+str(lM.acidMeasurement), ' '+str(lM.sugarMeasurement), lM.status, lM.timestamp.strftime("%d.%m.%Y - %H:%M"), lM.created_on.strftime("%d.%m.%Y - %H:%M")])

        return response

class ExportOrchardMeasurementsCSVByTreeId(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, treeId, *args, **kwargs):
        treeId = treeId
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="OrchardMeasurements_Tree_{}.csv"'.format(str(treeId))
        response.write(codecs.BOM_UTF8)

        writer = csv.writer(response, delimiter= ';', dialect = 'excel')
        orchardMeasurements = OrchardMeasurement.objects.filter(tree = treeId)

        #Headlines
        writer.writerow(['Tree ID', 'Variety Name', 'Frost Sensitivity', 'Growth Habit', 'Yield Habit', 'Temperature', 'Precipitation', 'Late Frost', 'Status', 'Created on'])

        #Rows
        for oM in orchardMeasurements:
            writer.writerow([oM.tree.id, oM.tree.variety.name, oM.frostSensitivity, oM.growthHabit, oM.yieldHabit, oM.temperature, oM.precipitation, oM.lateFrost, oM.status, oM.created_on.strftime("%d.%m.%Y - %H:%M")])

        return response

class ExportLabMeasurementsCSV(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="LabMeasurements.csv"'
        response.write(codecs.BOM_UTF8)

        writer = csv.writer(response, delimiter= ';', dialect = 'excel')
        location = self.request.query_params.get('location')
        labMeasurements = LabMeasurement.objects.all()

        if location is not None:
            labMeasurements = labMeasurements.filter(tree__location=location)

        #Headlines
        writer.writerow(['Tree ID', 'Variety Name', 'Strength Measurement', 'Flavor Measurement', 'Acid Measurement', 'Sugar Measurement', 'Status', 'Last Modified', 'Created on'])

        #Rows
        for lM in labMeasurements:
            writer.writerow([lM.tree.id, lM.tree.variety.name, ' '+str(lM.strengthMeasurement), lM.flavorMeasurement, ' '+str(lM.acidMeasurement), ' '+str(lM.sugarMeasurement), lM.status, lM.timestamp.strftime("%d.%m.%Y - %H:%M"), lM.created_on.strftime("%d.%m.%Y - %H:%M")])

        return response

class ExportOrchardMeasurementsCSV(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="OrchardMeasurements.csv"'
        response.write(codecs.BOM_UTF8)

        writer = csv.writer(response, delimiter= ';', dialect = 'excel')
        location = self.request.query_params.get('location')
        orchardMeasurements = OrchardMeasurement.objects.all()

        if location is not None:
            orchardMeasurements = orchardMeasurements.filter(tree__location=location)

        #Headlines
        writer.writerow(['Tree ID', 'Variety Name', 'Frost Sensitivity', 'Growth Habit', 'Yield Habit', 'Temperature', 'Precipitation', 'Late Frost', 'Status', 'Created on'])

        #Rows
        for oM in orchardMeasurements:
            writer.writerow([oM.tree.id, oM.tree.variety.name, oM.frostSensitivity, oM.growthHabit, oM.yieldHabit, oM.temperature, oM.precipitation, oM.lateFrost, oM.status, oM.created_on.strftime("%d.%m.%Y - %H:%M")])

        return response


class ExportTreesCSV(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
            response = HttpResponse(content_type='text/csv', charset='utf-8')
            response['Content-Disposition'] = 'attachment; filename="Trees.csv"'
            response.write(codecs.BOM_UTF8)

            writer = csv.writer(response, delimiter= ';', dialect = 'excel')
            location = self.request.query_params.get('location')
            trees = Tree.objects.all()

            if location is not None:
                trees = trees.filter(location=location)

            #Headlines
            writer.writerow(['Tree ID', 'Tree Type', 'Country', 'City', 'Row', 'Column', 'Planted on', 'Organic', 'Cut', 'Longitude', 'Latitude', 'Active', 'Variety ID', 'Variety Name', 'Blossom', 'Fruit', 'Climate', 'Pick Maturity', 'Usage', 'Bio', 'Pollinator', 'Properties', 'Output', 'Disease Possibility', 'Description'])

            #Rows
            for tree in trees:
                writer.writerow([tree.id, tree.type, tree.location.country, tree.location.city, tree.row, tree.column, tree.planted_on, tree.organic, tree.cut, tree.longitude, tree.latitude, tree.active, tree.variety.id, tree.variety.name, tree.variety.blossom, tree.variety.fruit, tree.variety.climate, tree.variety.pick_maturity, tree.variety.usage, tree.variety.bio, tree.variety.pollinator, tree.variety.properties, tree.variety.output, tree.variety.disease_possibility, tree.variety.description])

            return response