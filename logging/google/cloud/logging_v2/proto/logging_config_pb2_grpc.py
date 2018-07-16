# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import google.cloud.logging_v2.proto.logging_config_pb2 as google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ConfigServiceV2Stub(object):
  """Service for configuring sinks used to export log entries outside of
  Stackdriver Logging.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListSinks = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/ListSinks',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.ListSinksRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.ListSinksResponse.FromString,
        )
    self.GetSink = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/GetSink',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.GetSinkRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogSink.FromString,
        )
    self.CreateSink = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/CreateSink',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.CreateSinkRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogSink.FromString,
        )
    self.UpdateSink = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/UpdateSink',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.UpdateSinkRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogSink.FromString,
        )
    self.DeleteSink = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/DeleteSink',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.DeleteSinkRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListExclusions = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/ListExclusions',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.ListExclusionsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.ListExclusionsResponse.FromString,
        )
    self.GetExclusion = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/GetExclusion',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.GetExclusionRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogExclusion.FromString,
        )
    self.CreateExclusion = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/CreateExclusion',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.CreateExclusionRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogExclusion.FromString,
        )
    self.UpdateExclusion = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/UpdateExclusion',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.UpdateExclusionRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogExclusion.FromString,
        )
    self.DeleteExclusion = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/DeleteExclusion',
        request_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.DeleteExclusionRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ConfigServiceV2Servicer(object):
  """Service for configuring sinks used to export log entries outside of
  Stackdriver Logging.
  """

  def ListSinks(self, request, context):
    """Lists sinks.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSink(self, request, context):
    """Gets a sink.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateSink(self, request, context):
    """Creates a sink that exports specified log entries to a destination.  The
    export of newly-ingested log entries begins immediately, unless the sink's
    `writer_identity` is not permitted to write to the destination.  A sink can
    export log entries only from the resource owning the sink.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSink(self, request, context):
    """Updates a sink.  This method replaces the following fields in the existing
    sink with values from the new sink: `destination`, and `filter`.
    The updated sink might also have a new `writer_identity`; see the
    `unique_writer_identity` field.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSink(self, request, context):
    """Deletes a sink. If the sink has a unique `writer_identity`, then that
    service account is also deleted.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListExclusions(self, request, context):
    """Lists all the exclusions in a parent resource.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetExclusion(self, request, context):
    """Gets the description of an exclusion.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateExclusion(self, request, context):
    """Creates a new exclusion in a specified parent resource.
    Only log entries belonging to that resource can be excluded.
    You can have up to 10 exclusions in a resource.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateExclusion(self, request, context):
    """Changes one or more properties of an existing exclusion.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteExclusion(self, request, context):
    """Deletes an exclusion.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConfigServiceV2Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListSinks': grpc.unary_unary_rpc_method_handler(
          servicer.ListSinks,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.ListSinksRequest.FromString,
          response_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.ListSinksResponse.SerializeToString,
      ),
      'GetSink': grpc.unary_unary_rpc_method_handler(
          servicer.GetSink,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.GetSinkRequest.FromString,
          response_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogSink.SerializeToString,
      ),
      'CreateSink': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSink,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.CreateSinkRequest.FromString,
          response_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogSink.SerializeToString,
      ),
      'UpdateSink': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSink,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.UpdateSinkRequest.FromString,
          response_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogSink.SerializeToString,
      ),
      'DeleteSink': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSink,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.DeleteSinkRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListExclusions': grpc.unary_unary_rpc_method_handler(
          servicer.ListExclusions,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.ListExclusionsRequest.FromString,
          response_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.ListExclusionsResponse.SerializeToString,
      ),
      'GetExclusion': grpc.unary_unary_rpc_method_handler(
          servicer.GetExclusion,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.GetExclusionRequest.FromString,
          response_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogExclusion.SerializeToString,
      ),
      'CreateExclusion': grpc.unary_unary_rpc_method_handler(
          servicer.CreateExclusion,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.CreateExclusionRequest.FromString,
          response_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogExclusion.SerializeToString,
      ),
      'UpdateExclusion': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateExclusion,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.UpdateExclusionRequest.FromString,
          response_serializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.LogExclusion.SerializeToString,
      ),
      'DeleteExclusion': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteExclusion,
          request_deserializer=google_dot_cloud_dot_logging__v2_dot_proto_dot_logging__config__pb2.DeleteExclusionRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.logging.v2.ConfigServiceV2', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))