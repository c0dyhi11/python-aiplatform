# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.protobuf import struct_pb2 as struct  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.aiplatform.v1beta1',
    manifest={
        'Artifact',
    },
)


class Artifact(proto.Message):
    r"""Instance of a general artifact.

    Attributes:
        name (str):
            Output only. The resource name of the
            Artifact.
        display_name (str):
            User provided display name of the Artifact.
            May be up to 128 Unicode characters.
        uri (str):
            The uniform resource identifier of the
            artifact file. May be empty if there is no
            actual artifact file.
        etag (str):
            An eTag used to perform consistent read-
            odify-write updates. If not set, a blind
            "overwrite" update happens.
        labels (Sequence[google.cloud.aiplatform_v1beta1.types.Artifact.LabelsEntry]):
            The labels with user-defined metadata to organize your
            Artifacts.

            Label keys and values can be no longer than 64 characters
            (Unicode codepoints), can only contain lowercase letters,
            numeric characters, underscores and dashes. International
            characters are allowed. No more than 64 user labels can be
            associated with one Artifact (System labels are excluded).

            See https://goo.gl/xmQnxf for more information and examples
            of labels. System reserved label keys are prefixed with
            "aiplatform.googleapis.com/" and are immutable. Following
            system labels exist for each Artifact:

            -  "aiplatform.googleapis.com/schema_title":

               -  output only, its value is the title of the Artifact
                  schema provided either by [instance_schema_uri][] or
                  [instance_schema][].

            -  "aiplatform.googleapis.com/schema_version":

               -  output only, its value is the schema version of the
                  Artifact schema provided either by
                  [instance_schema_uri][] or [instance_schema][].
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this Artifact was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this Artifact was
            last updated.
        state (google.cloud.aiplatform_v1beta1.types.Artifact.State):
            The state of this Artifact. This is a
            property of the Artifact, and does not imply or
            capture any ongoing process. This property is
            managed by clients (such as AI Platform
            Pipelines), and the system does not prescribe or
            check the validity of state transitions.
        schema_title (str):
            The title of the schema describing the
            metadata.
            Schema title and version is expected to be
            registered in earlier Create Schema calls. And
            both are used together as unique identifiers to
            identify schemas within the local metadata
            store.
        schema_version (str):
            The version of the schema in schema_name to use.

            Schema title and version is expected to be registered in
            earlier Create Schema calls. And both are used together as
            unique identifiers to identify schemas within the local
            metadata store.
        metadata (google.protobuf.struct_pb2.Struct):
            Properties of the Artifact.
        description (str):
            Description of the Artifact
    """
    class State(proto.Enum):
        r"""Describes the state of the Artifact."""
        STATE_UNSPECIFIED = 0
        PENDING = 1
        LIVE = 2

    name = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)

    uri = proto.Field(proto.STRING, number=6)

    etag = proto.Field(proto.STRING, number=9)

    labels = proto.MapField(proto.STRING, proto.STRING, number=10)

    create_time = proto.Field(proto.MESSAGE, number=11,
        message=timestamp.Timestamp,
    )

    update_time = proto.Field(proto.MESSAGE, number=12,
        message=timestamp.Timestamp,
    )

    state = proto.Field(proto.ENUM, number=13,
        enum=State,
    )

    schema_title = proto.Field(proto.STRING, number=14)

    schema_version = proto.Field(proto.STRING, number=15)

    metadata = proto.Field(proto.MESSAGE, number=16,
        message=struct.Struct,
    )

    description = proto.Field(proto.STRING, number=17)


__all__ = tuple(sorted(__protobuf__.manifest))