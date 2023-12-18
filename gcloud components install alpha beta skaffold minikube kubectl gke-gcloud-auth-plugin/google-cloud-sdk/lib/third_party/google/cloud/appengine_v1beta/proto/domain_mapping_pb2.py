# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/appengine_v1beta/proto/domain_mapping.proto

from cloudsdk.google.protobuf import descriptor as _descriptor
from cloudsdk.google.protobuf import message as _message
from cloudsdk.google.protobuf import reflection as _reflection
from cloudsdk.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/appengine_v1beta/proto/domain_mapping.proto',
  package='google.appengine.v1beta',
  syntax='proto3',
  serialized_options=b'\n\033com.google.appengine.v1betaB\022DomainMappingProtoP\001Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/cloud/appengine_v1beta/proto/domain_mapping.proto\x12\x17google.appengine.v1beta\x1a\x1cgoogle/api/annotations.proto\"\xa8\x01\n\rDomainMapping\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12:\n\x0cssl_settings\x18\x03 \x01(\x0b\x32$.google.appengine.v1beta.SslSettings\x12\x41\n\x10resource_records\x18\x04 \x03(\x0b\x32\'.google.appengine.v1beta.ResourceRecord\"\xd2\x01\n\x0bSslSettings\x12\x16\n\x0e\x63\x65rtificate_id\x18\x01 \x01(\t\x12S\n\x13ssl_management_type\x18\x03 \x01(\x0e\x32\x36.google.appengine.v1beta.SslSettings.SslManagementType\x12&\n\x1epending_managed_certificate_id\x18\x04 \x01(\t\".\n\x11SslManagementType\x12\r\n\tAUTOMATIC\x10\x00\x12\n\n\x06MANUAL\x10\x01\"\x9a\x01\n\x0eResourceRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06rrdata\x18\x02 \x01(\t\x12@\n\x04type\x18\x03 \x01(\x0e\x32\x32.google.appengine.v1beta.ResourceRecord.RecordType\"(\n\nRecordType\x12\x05\n\x01\x41\x10\x00\x12\x08\n\x04\x41\x41\x41\x41\x10\x01\x12\t\n\x05\x43NAME\x10\x02\x42u\n\x1b\x63om.google.appengine.v1betaB\x12\x44omainMappingProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengineb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_SSLSETTINGS_SSLMANAGEMENTTYPE = _descriptor.EnumDescriptor(
  name='SslManagementType',
  full_name='google.appengine.v1beta.SslSettings.SslManagementType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTOMATIC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MANUAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=451,
  serialized_end=497,
)
_sym_db.RegisterEnumDescriptor(_SSLSETTINGS_SSLMANAGEMENTTYPE)

_RESOURCERECORD_RECORDTYPE = _descriptor.EnumDescriptor(
  name='RecordType',
  full_name='google.appengine.v1beta.ResourceRecord.RecordType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='A', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AAAA', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CNAME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=614,
  serialized_end=654,
)
_sym_db.RegisterEnumDescriptor(_RESOURCERECORD_RECORDTYPE)


_DOMAINMAPPING = _descriptor.Descriptor(
  name='DomainMapping',
  full_name='google.appengine.v1beta.DomainMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.appengine.v1beta.DomainMapping.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.appengine.v1beta.DomainMapping.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssl_settings', full_name='google.appengine.v1beta.DomainMapping.ssl_settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_records', full_name='google.appengine.v1beta.DomainMapping.resource_records', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=284,
)


_SSLSETTINGS = _descriptor.Descriptor(
  name='SslSettings',
  full_name='google.appengine.v1beta.SslSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='certificate_id', full_name='google.appengine.v1beta.SslSettings.certificate_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssl_management_type', full_name='google.appengine.v1beta.SslSettings.ssl_management_type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending_managed_certificate_id', full_name='google.appengine.v1beta.SslSettings.pending_managed_certificate_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SSLSETTINGS_SSLMANAGEMENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=497,
)


_RESOURCERECORD = _descriptor.Descriptor(
  name='ResourceRecord',
  full_name='google.appengine.v1beta.ResourceRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.appengine.v1beta.ResourceRecord.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rrdata', full_name='google.appengine.v1beta.ResourceRecord.rrdata', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.appengine.v1beta.ResourceRecord.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESOURCERECORD_RECORDTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=654,
)

_DOMAINMAPPING.fields_by_name['ssl_settings'].message_type = _SSLSETTINGS
_DOMAINMAPPING.fields_by_name['resource_records'].message_type = _RESOURCERECORD
_SSLSETTINGS.fields_by_name['ssl_management_type'].enum_type = _SSLSETTINGS_SSLMANAGEMENTTYPE
_SSLSETTINGS_SSLMANAGEMENTTYPE.containing_type = _SSLSETTINGS
_RESOURCERECORD.fields_by_name['type'].enum_type = _RESOURCERECORD_RECORDTYPE
_RESOURCERECORD_RECORDTYPE.containing_type = _RESOURCERECORD
DESCRIPTOR.message_types_by_name['DomainMapping'] = _DOMAINMAPPING
DESCRIPTOR.message_types_by_name['SslSettings'] = _SSLSETTINGS
DESCRIPTOR.message_types_by_name['ResourceRecord'] = _RESOURCERECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DomainMapping = _reflection.GeneratedProtocolMessageType('DomainMapping', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINMAPPING,
  '__module__' : 'google.cloud.appengine_v1beta.proto.domain_mapping_pb2'
  ,
  '__doc__': """A domain serving an App Engine application.
  
  Attributes:
      name:
          Full path to the ``DomainMapping`` resource in the API.
          Example: ``apps/myapp/domainMapping/example.com``.
          @OutputOnly
      id:
          Relative name of the domain serving the application. Example:
          ``example.com``.
      ssl_settings:
          SSL configuration for this domain. If unconfigured, this
          domain will not serve with SSL.
      resource_records:
          The resource records required to configure this domain
          mapping. These records must be added to the domain’s DNS
          configuration in order to serve the application via this
          domain mapping.  @OutputOnly
  """,
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.DomainMapping)
  })
_sym_db.RegisterMessage(DomainMapping)

SslSettings = _reflection.GeneratedProtocolMessageType('SslSettings', (_message.Message,), {
  'DESCRIPTOR' : _SSLSETTINGS,
  '__module__' : 'google.cloud.appengine_v1beta.proto.domain_mapping_pb2'
  ,
  '__doc__': """SSL configuration for a ``DomainMapping`` resource.
  
  Attributes:
      certificate_id:
          ID of the ``AuthorizedCertificate`` resource configuring SSL
          for the application. Clearing this field will remove SSL
          support.  By default, a managed certificate is automatically
          created for every domain mapping. To omit SSL support or to
          configure SSL manually, specify ``SslManagementType.MANUAL``
          on a ``CREATE`` or ``UPDATE`` request. You must be authorized
          to administer the ``AuthorizedCertificate`` resource to
          manually map it to a ``DomainMapping`` resource. Example:
          ``12345``.
      ssl_management_type:
          SSL management type for this domain. If ``AUTOMATIC``, a
          managed certificate is automatically provisioned. If
          ``MANUAL``, ``certificate_id`` must be manually specified in
          order to configure SSL for this domain.
      pending_managed_certificate_id:
          ID of the managed ``AuthorizedCertificate`` resource currently
          being provisioned, if applicable. Until the new managed
          certificate has been successfully provisioned, the previous
          SSL state will be preserved. Once the provisioning process
          completes, the ``certificate_id`` field will reflect the new
          managed certificate and this field will be left empty. To
          remove SSL support while there is still a pending managed
          certificate, clear the ``certificate_id`` field with an
          ``UpdateDomainMappingRequest``.  @OutputOnly
  """,
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.SslSettings)
  })
_sym_db.RegisterMessage(SslSettings)

ResourceRecord = _reflection.GeneratedProtocolMessageType('ResourceRecord', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCERECORD,
  '__module__' : 'google.cloud.appengine_v1beta.proto.domain_mapping_pb2'
  ,
  '__doc__': """A DNS resource record.
  
  Attributes:
      name:
          Relative name of the object affected by this record. Only
          applicable for ``CNAME`` records. Example: ‘www’.
      rrdata:
          Data for this record. Values vary by record type, as defined
          in RFC 1035 (section 5) and RFC 1034 (section 3.6.1).
      type:
          Resource record type. Example: ``AAAA``.
  """,
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.ResourceRecord)
  })
_sym_db.RegisterMessage(ResourceRecord)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
