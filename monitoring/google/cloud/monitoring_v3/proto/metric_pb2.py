# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/metric.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import distribution_pb2 as google_dot_api_dot_distribution__pb2
from google.api import label_pb2 as google_dot_api_dot_label__pb2
from google.api import metric_pb2 as google_dot_api_dot_metric__pb2
from google.api import (
    monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2,
)
from google.cloud.monitoring_v3.proto import (
    common_pb2 as google_dot_cloud_dot_monitoring__v3_dot_proto_dot_common__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_v3/proto/metric.proto",
    package="google.monitoring.v3",
    syntax="proto3",
    serialized_options=_b(
        "\n\030com.google.monitoring.v3B\013MetricProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3"
    ),
    serialized_pb=_b(
        '\n-google/cloud/monitoring_v3/proto/metric.proto\x12\x14google.monitoring.v3\x1a\x1dgoogle/api/distribution.proto\x1a\x16google/api/label.proto\x1a\x17google/api/metric.proto\x1a#google/api/monitored_resource.proto\x1a-google/cloud/monitoring_v3/proto/common.proto"n\n\x05Point\x12\x34\n\x08interval\x18\x01 \x01(\x0b\x32".google.monitoring.v3.TimeInterval\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .google.monitoring.v3.TypedValue"\xc1\x02\n\nTimeSeries\x12"\n\x06metric\x18\x01 \x01(\x0b\x32\x12.google.api.Metric\x12/\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.google.api.MonitoredResource\x12\x37\n\x08metadata\x18\x07 \x01(\x0b\x32%.google.api.MonitoredResourceMetadata\x12<\n\x0bmetric_kind\x18\x03 \x01(\x0e\x32\'.google.api.MetricDescriptor.MetricKind\x12:\n\nvalue_type\x18\x04 \x01(\x0e\x32&.google.api.MetricDescriptor.ValueType\x12+\n\x06points\x18\x05 \x03(\x0b\x32\x1b.google.monitoring.v3.PointB\xa3\x01\n\x18\x63om.google.monitoring.v3B\x0bMetricProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_distribution__pb2.DESCRIPTOR,
        google_dot_api_dot_label__pb2.DESCRIPTOR,
        google_dot_api_dot_metric__pb2.DESCRIPTOR,
        google_dot_api_dot_monitored__resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_monitoring__v3_dot_proto_dot_common__pb2.DESCRIPTOR,
    ],
)


_POINT = _descriptor.Descriptor(
    name="Point",
    full_name="google.monitoring.v3.Point",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="interval",
            full_name="google.monitoring.v3.Point.interval",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.monitoring.v3.Point.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=235,
    serialized_end=345,
)


_TIMESERIES = _descriptor.Descriptor(
    name="TimeSeries",
    full_name="google.monitoring.v3.TimeSeries",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="metric",
            full_name="google.monitoring.v3.TimeSeries.metric",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="resource",
            full_name="google.monitoring.v3.TimeSeries.resource",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="google.monitoring.v3.TimeSeries.metadata",
            index=2,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="metric_kind",
            full_name="google.monitoring.v3.TimeSeries.metric_kind",
            index=3,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value_type",
            full_name="google.monitoring.v3.TimeSeries.value_type",
            index=4,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="points",
            full_name="google.monitoring.v3.TimeSeries.points",
            index=5,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=348,
    serialized_end=669,
)

_POINT.fields_by_name[
    "interval"
].message_type = (
    google_dot_cloud_dot_monitoring__v3_dot_proto_dot_common__pb2._TIMEINTERVAL
)
_POINT.fields_by_name[
    "value"
].message_type = (
    google_dot_cloud_dot_monitoring__v3_dot_proto_dot_common__pb2._TYPEDVALUE
)
_TIMESERIES.fields_by_name[
    "metric"
].message_type = google_dot_api_dot_metric__pb2._METRIC
_TIMESERIES.fields_by_name[
    "resource"
].message_type = google_dot_api_dot_monitored__resource__pb2._MONITOREDRESOURCE
_TIMESERIES.fields_by_name[
    "metadata"
].message_type = google_dot_api_dot_monitored__resource__pb2._MONITOREDRESOURCEMETADATA
_TIMESERIES.fields_by_name[
    "metric_kind"
].enum_type = google_dot_api_dot_metric__pb2._METRICDESCRIPTOR_METRICKIND
_TIMESERIES.fields_by_name[
    "value_type"
].enum_type = google_dot_api_dot_metric__pb2._METRICDESCRIPTOR_VALUETYPE
_TIMESERIES.fields_by_name["points"].message_type = _POINT
DESCRIPTOR.message_types_by_name["Point"] = _POINT
DESCRIPTOR.message_types_by_name["TimeSeries"] = _TIMESERIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point = _reflection.GeneratedProtocolMessageType(
    "Point",
    (_message.Message,),
    dict(
        DESCRIPTOR=_POINT,
        __module__="google.cloud.monitoring_v3.proto.metric_pb2",
        __doc__="""A single data point in a time series.
  
  
  Attributes:
      interval:
          The time interval to which the data point applies. For
          ``GAUGE`` metrics, only the end time of the interval is used.
          For ``DELTA`` metrics, the start and end time should specify a
          non-zero interval, with subsequent points specifying
          contiguous and non-overlapping intervals. For ``CUMULATIVE``
          metrics, the start and end time should specify a non-zero
          interval, with subsequent points specifying the same start
          time and increasing end times, until an event resets the
          cumulative value to zero and sets a new start time for the
          following points.
      value:
          The value of the data point.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.Point)
    ),
)
_sym_db.RegisterMessage(Point)

TimeSeries = _reflection.GeneratedProtocolMessageType(
    "TimeSeries",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TIMESERIES,
        __module__="google.cloud.monitoring_v3.proto.metric_pb2",
        __doc__="""A collection of data points that describes the time-varying values of a
  metric. A time series is identified by a combination of a
  fully-specified monitored resource and a fully-specified metric. This
  type is used for both listing and creating time series.
  
  
  Attributes:
      metric:
          The associated metric. A fully-specified metric used to
          identify the time series.
      resource:
          The associated monitored resource. Custom metrics can use only
          certain monitored resource types in their time series data.
      metadata:
          Output only. The associated monitored resource metadata. When
          reading a a timeseries, this field will include metadata
          labels that are explicitly named in the reduction. When
          creating a timeseries, this field is ignored.
      metric_kind:
          The metric kind of the time series. When listing time series,
          this metric kind might be different from the metric kind of
          the associated metric if this time series is an alignment or
          reduction of other time series.  When creating a time series,
          this field is optional. If present, it must be the same as the
          metric kind of the associated metric. If the associated
          metric's descriptor must be auto-created, then this field
          specifies the metric kind of the new descriptor and must be
          either ``GAUGE`` (the default) or ``CUMULATIVE``.
      value_type:
          The value type of the time series. When listing time series,
          this value type might be different from the value type of the
          associated metric if this time series is an alignment or
          reduction of other time series.  When creating a time series,
          this field is optional. If present, it must be the same as the
          type of the data in the ``points`` field.
      points:
          The data points of this time series. When listing time series,
          points are returned in reverse time order.  When creating a
          time series, this field must contain exactly one point and the
          point's type must be the same as the value type of the
          associated metric. If the associated metric's descriptor must
          be auto-created, then the value type of the descriptor is
          determined by the point's type, which must be ``BOOL``,
          ``INT64``, ``DOUBLE``, or ``DISTRIBUTION``.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.TimeSeries)
    ),
)
_sym_db.RegisterMessage(TimeSeries)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
