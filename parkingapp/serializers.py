from rest_framework import serializers

from .models import ParkingSpot, ParkingFloor, ParkingLot, PaymentCounter, EntryGate, ExitGate, DisplayBoard, Operators, Address

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'


    def create(self, validated_data):
        return ParkingSpot.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.spot_type = validated_data.get('spot_type', instance.spot_type)
        instance.spot_status = validated_data.get('spot_status', instance.spot_status)
        instance.save()
        return instance




class ParkingFloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingFloor
        fields = '__all__'


    def create(self, validated_data):
        return ParkingFloor.objects.create(**validated_data)


    def get(self, validated_data):
        return ParkingFloor.objects.get(**validated_data)




class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = '__all__'

    def create(self, validated_data):

        return ParkingLot.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.parking_floor = validated_data.get('parking_floor', instance.parking_floor)
        instance.entry_gate = validated_data.get('entry_gate', instance.entry_gate)
        instance.exit_gate = validated_data.get('exit_gate', instance.exit_gate)
        instance.save()
        return instance



class PaymentCounterSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentCounter
        fields = '__all__'

    def create(self, validated_data):
        return PaymentCounter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.counter_number = validated_data.get('counter_number', instance.counter_number)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance


class EntryGateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryGate
        fields = '__all__'

    def create(self, validated_data):
        return EntryGate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.operators = validated_data.get('operators', instance.operators)
        instance.save()
        return instance


class ExitGateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExitGate
        fields = '__all__'

    def create(self, validated_data):
        return ExitGate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.operators = validated_data.get('operators', instance.operators)
        instance.save()
        return instance


class DisplayBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayBoard
        fields = '__all__'

    def create(self, validated_data):
        return DisplayBoard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance

class OperatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operators
        fields = '__all__'

    def create(self, validated_data):
        return Operators.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.save()
        return instance


