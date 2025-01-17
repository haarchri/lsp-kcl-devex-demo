# generated by datamodel-codegen:
#   filename:  workdir/s3_aws_upbound_io_v1beta1_bucketinventory.yaml

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import AwareDatetime, BaseModel, Field

from .....k8s.apimachinery.pkg.apis.meta import v1


class DeletionPolicy(Enum):
    Orphan = 'Orphan'
    Delete = 'Delete'


class Resolution(Enum):
    Required = 'Required'
    Optional = 'Optional'


class Resolve(Enum):
    Always = 'Always'
    IfNotPresent = 'IfNotPresent'


class Policy(BaseModel):
    resolution: Optional[Resolution] = 'Required'
    """
    Resolution specifies whether resolution of this reference is required.
    The default is 'Required', which means the reconcile will fail if the
    reference cannot be resolved. 'Optional' means this reference will be
    a no-op if it cannot be resolved.
    """
    resolve: Optional[Resolve] = None
    """
    Resolve specifies when this reference should be resolved. The default
    is 'IfNotPresent', which will attempt to resolve the reference only when
    the corresponding field is not present. Use 'Always' to resolve the
    reference on every reconcile.
    """


class BucketRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class BucketSelector(BaseModel):
    matchControllerRef: Optional[bool] = None
    """
    MatchControllerRef ensures an object with the same controller reference
    as the selecting object is selected.
    """
    matchLabels: Optional[Dict[str, str]] = None
    """
    MatchLabels ensures an object with matching labels is selected.
    """
    policy: Optional[Policy] = None
    """
    Policies for selection.
    """


class BucketArnRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class BucketArnSelector(BaseModel):
    matchControllerRef: Optional[bool] = None
    """
    MatchControllerRef ensures an object with the same controller reference
    as the selecting object is selected.
    """
    matchLabels: Optional[Dict[str, str]] = None
    """
    MatchLabels ensures an object with matching labels is selected.
    """
    policy: Optional[Policy] = None
    """
    Policies for selection.
    """


class SseKm(BaseModel):
    keyId: Optional[str] = None
    """
    ARN of the KMS customer master key (CMK) used to encrypt the inventory file.
    """


class EncryptionItem(BaseModel):
    sseKms: Optional[List[SseKm]] = None
    """
    Specifies to use server-side encryption with AWS KMS-managed keys to encrypt the inventory file (documented below).
    """
    sseS3: Optional[List[Dict[str, Any]]] = None
    """
    Specifies to use server-side encryption with Amazon S3-managed keys (SSE-S3) to encrypt the inventory file.
    """


class BucketItem(BaseModel):
    accountId: Optional[str] = None
    """
    ID of the account that owns the destination bucket. Recommended to be set to prevent problems if the destination bucket ownership changes.
    """
    bucketArn: Optional[str] = None
    """
    Amazon S3 bucket ARN of the destination.
    """
    bucketArnRef: Optional[BucketArnRef] = None
    """
    Reference to a Bucket in s3 to populate bucketArn.
    """
    bucketArnSelector: Optional[BucketArnSelector] = None
    """
    Selector for a Bucket in s3 to populate bucketArn.
    """
    encryption: Optional[List[EncryptionItem]] = None
    """
    Contains the type of server-side encryption to use to encrypt the inventory (documented below).
    """
    format: Optional[str] = None
    """
    Specifies the output format of the inventory results. Can be CSV, ORC or Parquet.
    """
    prefix: Optional[str] = None
    """
    Prefix that an object must have to be included in the inventory results.
    """


class DestinationItem(BaseModel):
    bucket: Optional[List[BucketItem]] = None
    """
    Name of the source bucket that inventory lists the objects for.
    """


class FilterItem(BaseModel):
    prefix: Optional[str] = None
    """
    Prefix that an object must have to be included in the inventory results.
    """


class ScheduleItem(BaseModel):
    frequency: Optional[str] = None
    """
    Specifies how frequently inventory results are produced. Valid values: Daily, Weekly.
    """


class ForProvider(BaseModel):
    bucket: Optional[str] = None
    """
    Name of the source bucket that inventory lists the objects for.
    """
    bucketRef: Optional[BucketRef] = None
    """
    Reference to a Bucket in s3 to populate bucket.
    """
    bucketSelector: Optional[BucketSelector] = None
    """
    Selector for a Bucket in s3 to populate bucket.
    """
    destination: Optional[List[DestinationItem]] = None
    """
    Contains information about where to publish the inventory results (documented below).
    """
    enabled: Optional[bool] = None
    """
    Specifies whether the inventory is enabled or disabled.
    """
    filter: Optional[List[FilterItem]] = None
    """
    Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria (documented below).
    """
    includedObjectVersions: Optional[str] = None
    """
    Object versions to include in the inventory list. Valid values: All, Current.
    """
    name: Optional[str] = None
    """
    Unique identifier of the inventory configuration for the bucket.
    """
    optionalFields: Optional[List[str]] = None
    """
    List of optional fields that are included in the inventory results. Please refer to the S3 documentation for more details.
    """
    region: str
    """
    Region is the region you'd like your resource to be created in.
    """
    schedule: Optional[List[ScheduleItem]] = None
    """
    Specifies the schedule for generating inventory results (documented below).
    """


class InitProvider(BaseModel):
    bucket: Optional[str] = None
    """
    Name of the source bucket that inventory lists the objects for.
    """
    bucketRef: Optional[BucketRef] = None
    """
    Reference to a Bucket in s3 to populate bucket.
    """
    bucketSelector: Optional[BucketSelector] = None
    """
    Selector for a Bucket in s3 to populate bucket.
    """
    destination: Optional[List[DestinationItem]] = None
    """
    Contains information about where to publish the inventory results (documented below).
    """
    enabled: Optional[bool] = None
    """
    Specifies whether the inventory is enabled or disabled.
    """
    filter: Optional[List[FilterItem]] = None
    """
    Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria (documented below).
    """
    includedObjectVersions: Optional[str] = None
    """
    Object versions to include in the inventory list. Valid values: All, Current.
    """
    name: Optional[str] = None
    """
    Unique identifier of the inventory configuration for the bucket.
    """
    optionalFields: Optional[List[str]] = None
    """
    List of optional fields that are included in the inventory results. Please refer to the S3 documentation for more details.
    """
    schedule: Optional[List[ScheduleItem]] = None
    """
    Specifies the schedule for generating inventory results (documented below).
    """


class ManagementPolicy(Enum):
    Observe = 'Observe'
    Create = 'Create'
    Update = 'Update'
    Delete = 'Delete'
    LateInitialize = 'LateInitialize'
    field_ = '*'


class ProviderConfigRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class ConfigRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class Metadata(BaseModel):
    annotations: Optional[Dict[str, str]] = None
    """
    Annotations are the annotations to be added to connection secret.
    - For Kubernetes secrets, this will be used as "metadata.annotations".
    - It is up to Secret Store implementation for others store types.
    """
    labels: Optional[Dict[str, str]] = None
    """
    Labels are the labels/tags to be added to connection secret.
    - For Kubernetes secrets, this will be used as "metadata.labels".
    - It is up to Secret Store implementation for others store types.
    """
    type: Optional[str] = None
    """
    Type is the SecretType for the connection secret.
    - Only valid for Kubernetes Secret Stores.
    """


class PublishConnectionDetailsTo(BaseModel):
    configRef: Optional[ConfigRef] = Field(
        default_factory=lambda: ConfigRef.model_validate({'name': 'default'})
    )
    """
    SecretStoreConfigRef specifies which secret store config should be used
    for this ConnectionSecret.
    """
    metadata: Optional[Metadata] = None
    """
    Metadata is the metadata for connection secret.
    """
    name: str
    """
    Name is the name of the connection secret.
    """


class WriteConnectionSecretToRef(BaseModel):
    name: str
    """
    Name of the secret.
    """
    namespace: str
    """
    Namespace of the secret.
    """


class Spec(BaseModel):
    deletionPolicy: Optional[DeletionPolicy] = 'Delete'
    """
    DeletionPolicy specifies what will happen to the underlying external
    when this managed resource is deleted - either "Delete" or "Orphan" the
    external resource.
    This field is planned to be deprecated in favor of the ManagementPolicies
    field in a future release. Currently, both could be set independently and
    non-default values would be honored if the feature flag is enabled.
    See the design doc for more information: https://github.com/crossplane/crossplane/blob/499895a25d1a1a0ba1604944ef98ac7a1a71f197/design/design-doc-observe-only-resources.md?plain=1#L223
    """
    forProvider: ForProvider
    initProvider: Optional[InitProvider] = None
    """
    THIS IS A BETA FIELD. It will be honored
    unless the Management Policies feature flag is disabled.
    InitProvider holds the same fields as ForProvider, with the exception
    of Identifier and other resource reference fields. The fields that are
    in InitProvider are merged into ForProvider when the resource is created.
    The same fields are also added to the terraform ignore_changes hook, to
    avoid updating them after creation. This is useful for fields that are
    required on creation, but we do not desire to update them after creation,
    for example because of an external controller is managing them, like an
    autoscaler.
    """
    managementPolicies: Optional[List[ManagementPolicy]] = ['*']
    """
    THIS IS A BETA FIELD. It is on by default but can be opted out
    through a Crossplane feature flag.
    ManagementPolicies specify the array of actions Crossplane is allowed to
    take on the managed and external resources.
    This field is planned to replace the DeletionPolicy field in a future
    release. Currently, both could be set independently and non-default
    values would be honored if the feature flag is enabled. If both are
    custom, the DeletionPolicy field will be ignored.
    See the design doc for more information: https://github.com/crossplane/crossplane/blob/499895a25d1a1a0ba1604944ef98ac7a1a71f197/design/design-doc-observe-only-resources.md?plain=1#L223
    and this one: https://github.com/crossplane/crossplane/blob/444267e84783136daa93568b364a5f01228cacbe/design/one-pager-ignore-changes.md
    """
    providerConfigRef: Optional[ProviderConfigRef] = Field(
        default_factory=lambda: ProviderConfigRef.model_validate({'name': 'default'})
    )
    """
    ProviderConfigReference specifies how the provider that will be used to
    create, observe, update, and delete this managed resource should be
    configured.
    """
    publishConnectionDetailsTo: Optional[PublishConnectionDetailsTo] = None
    """
    PublishConnectionDetailsTo specifies the connection secret config which
    contains a name, metadata and a reference to secret store config to
    which any connection details for this managed resource should be written.
    Connection details frequently include the endpoint, username,
    and password required to connect to the managed resource.
    """
    writeConnectionSecretToRef: Optional[WriteConnectionSecretToRef] = None
    """
    WriteConnectionSecretToReference specifies the namespace and name of a
    Secret to which any connection details for this managed resource should
    be written. Connection details frequently include the endpoint, username,
    and password required to connect to the managed resource.
    This field is planned to be replaced in a future release in favor of
    PublishConnectionDetailsTo. Currently, both could be set independently
    and connection details would be published to both without affecting
    each other.
    """


class BucketItemModel(BaseModel):
    accountId: Optional[str] = None
    """
    ID of the account that owns the destination bucket. Recommended to be set to prevent problems if the destination bucket ownership changes.
    """
    bucketArn: Optional[str] = None
    """
    Amazon S3 bucket ARN of the destination.
    """
    encryption: Optional[List[EncryptionItem]] = None
    """
    Contains the type of server-side encryption to use to encrypt the inventory (documented below).
    """
    format: Optional[str] = None
    """
    Specifies the output format of the inventory results. Can be CSV, ORC or Parquet.
    """
    prefix: Optional[str] = None
    """
    Prefix that an object must have to be included in the inventory results.
    """


class AtProvider(BaseModel):
    bucket: Optional[str] = None
    """
    Name of the source bucket that inventory lists the objects for.
    """
    destination: Optional[List[DestinationItem]] = None
    """
    Contains information about where to publish the inventory results (documented below).
    """
    enabled: Optional[bool] = None
    """
    Specifies whether the inventory is enabled or disabled.
    """
    filter: Optional[List[FilterItem]] = None
    """
    Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria (documented below).
    """
    id: Optional[str] = None
    includedObjectVersions: Optional[str] = None
    """
    Object versions to include in the inventory list. Valid values: All, Current.
    """
    name: Optional[str] = None
    """
    Unique identifier of the inventory configuration for the bucket.
    """
    optionalFields: Optional[List[str]] = None
    """
    List of optional fields that are included in the inventory results. Please refer to the S3 documentation for more details.
    """
    schedule: Optional[List[ScheduleItem]] = None
    """
    Specifies the schedule for generating inventory results (documented below).
    """


class Condition(BaseModel):
    lastTransitionTime: AwareDatetime
    """
    LastTransitionTime is the last time this condition transitioned from one
    status to another.
    """
    message: Optional[str] = None
    """
    A Message containing details about this condition's last transition from
    one status to another, if any.
    """
    observedGeneration: Optional[int] = None
    """
    ObservedGeneration represents the .metadata.generation that the condition was set based upon.
    For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
    with respect to the current state of the instance.
    """
    reason: str
    """
    A Reason for this condition's last transition from one status to another.
    """
    status: str
    """
    Status of this condition; is it currently True, False, or Unknown?
    """
    type: str
    """
    Type of this condition. At most one of each condition type may apply to
    a resource at any point in time.
    """


class Status(BaseModel):
    atProvider: Optional[AtProvider] = None
    conditions: Optional[List[Condition]] = None
    """
    Conditions of the resource.
    """
    observedGeneration: Optional[int] = None
    """
    ObservedGeneration is the latest metadata.generation
    which resulted in either a ready state, or stalled due to error
    it can not recover from without human intervention.
    """


class BucketInventory(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Spec
    """
    BucketInventorySpec defines the desired state of BucketInventory
    """
    status: Optional[Status] = None
    """
    BucketInventoryStatus defines the observed state of BucketInventory.
    """


class BucketInventoryList(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    items: List[BucketInventory]
    """
    List of bucketinventories. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ListMeta] = None
    """
    Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """