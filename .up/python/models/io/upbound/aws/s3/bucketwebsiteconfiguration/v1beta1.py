# generated by datamodel-codegen:
#   filename:  workdir/s3_aws_upbound_io_v1beta1_bucketwebsiteconfiguration.yaml

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

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


class ErrorDocumentItem(BaseModel):
    key: Optional[str] = None
    """
    Object key name to use when a 4XX class error occurs.
    """


class IndexDocumentItem(BaseModel):
    suffix: Optional[str] = None
    """
    Suffix that is appended to a request that is for a directory on the website endpoint.
    For example, if the suffix is index.html and you make a request to samplebucket/images/, the data that is returned will be for the object with the key name images/index.html.
    The suffix must not be empty and must not include a slash character.
    """


class RedirectAllRequestsToItem(BaseModel):
    hostName: Optional[str] = None
    """
    Name of the host where requests are redirected.
    """
    protocol: Optional[str] = None
    """
    Protocol to use when redirecting requests. The default is the protocol that is used in the original request. Valid values: http, https.
    """


class ConditionItem(BaseModel):
    httpErrorCodeReturnedEquals: Optional[str] = None
    """
    HTTP error code when the redirect is applied. If specified with key_prefix_equals, then both must be true for the redirect to be applied.
    """
    keyPrefixEquals: Optional[str] = None
    """
    Object key name prefix when the redirect is applied. If specified with http_error_code_returned_equals, then both must be true for the redirect to be applied.
    """


class RedirectItem(BaseModel):
    hostName: Optional[str] = None
    """
    Name of the host where requests are redirected.
    """
    httpRedirectCode: Optional[str] = None
    """
    HTTP redirect code to use on the response.
    """
    protocol: Optional[str] = None
    """
    Protocol to use when redirecting requests. The default is the protocol that is used in the original request. Valid values: http, https.
    """
    replaceKeyPrefixWith: Optional[str] = None
    """
    Object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix docs/ (objects in the docs/ folder) to documents/, you can set a condition block with key_prefix_equals set to docs/ and in the redirect set replace_key_prefix_with to /documents.
    """
    replaceKeyWith: Optional[str] = None
    """
    Specific object key to use in the redirect request. For example, redirect request to error.html.
    """


class RoutingRuleItem(BaseModel):
    condition: Optional[List[ConditionItem]] = None
    """
    Configuration block for describing a condition that must be met for the specified redirect to apply. See below.
    """
    redirect: Optional[List[RedirectItem]] = None
    """
    Configuration block for redirect information. See below.
    """


class ForProvider(BaseModel):
    bucket: Optional[str] = None
    """
    Name of the bucket.
    """
    bucketRef: Optional[BucketRef] = None
    """
    Reference to a Bucket in s3 to populate bucket.
    """
    bucketSelector: Optional[BucketSelector] = None
    """
    Selector for a Bucket in s3 to populate bucket.
    """
    errorDocument: Optional[List[ErrorDocumentItem]] = None
    """
    Name of the error document for the website. See below.
    """
    expectedBucketOwner: Optional[str] = None
    """
    Account ID of the expected bucket owner.
    """
    indexDocument: Optional[List[IndexDocumentItem]] = None
    """
    Name of the index document for the website. See below.
    """
    redirectAllRequestsTo: Optional[List[RedirectAllRequestsToItem]] = None
    """
    Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with error_document, index_document, and routing_rule.
    """
    region: str
    """
    Region is the region you'd like your resource to be created in.
    """
    routingRule: Optional[List[RoutingRuleItem]] = None
    """
    List of rules that define when a redirect is applied and the redirect behavior. See below.
    """
    routingRules: Optional[str] = None
    """
    JSON array containing routing rules
    describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values ("") as seen in the example above.
    """


class InitProvider(BaseModel):
    bucket: Optional[str] = None
    """
    Name of the bucket.
    """
    bucketRef: Optional[BucketRef] = None
    """
    Reference to a Bucket in s3 to populate bucket.
    """
    bucketSelector: Optional[BucketSelector] = None
    """
    Selector for a Bucket in s3 to populate bucket.
    """
    errorDocument: Optional[List[ErrorDocumentItem]] = None
    """
    Name of the error document for the website. See below.
    """
    expectedBucketOwner: Optional[str] = None
    """
    Account ID of the expected bucket owner.
    """
    indexDocument: Optional[List[IndexDocumentItem]] = None
    """
    Name of the index document for the website. See below.
    """
    redirectAllRequestsTo: Optional[List[RedirectAllRequestsToItem]] = None
    """
    Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with error_document, index_document, and routing_rule.
    """
    routingRule: Optional[List[RoutingRuleItem]] = None
    """
    List of rules that define when a redirect is applied and the redirect behavior. See below.
    """
    routingRules: Optional[str] = None
    """
    JSON array containing routing rules
    describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values ("") as seen in the example above.
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


class AtProvider(BaseModel):
    bucket: Optional[str] = None
    """
    Name of the bucket.
    """
    errorDocument: Optional[List[ErrorDocumentItem]] = None
    """
    Name of the error document for the website. See below.
    """
    expectedBucketOwner: Optional[str] = None
    """
    Account ID of the expected bucket owner.
    """
    id: Optional[str] = None
    """
    The bucket or bucket and expected_bucket_owner separated by a comma (,) if the latter is provided.
    """
    indexDocument: Optional[List[IndexDocumentItem]] = None
    """
    Name of the index document for the website. See below.
    """
    redirectAllRequestsTo: Optional[List[RedirectAllRequestsToItem]] = None
    """
    Redirect behavior for every request to this bucket's website endpoint. See below. Conflicts with error_document, index_document, and routing_rule.
    """
    routingRule: Optional[List[RoutingRuleItem]] = None
    """
    List of rules that define when a redirect is applied and the redirect behavior. See below.
    """
    routingRules: Optional[str] = None
    """
    JSON array containing routing rules
    describing redirect behavior and when redirects are applied. Use this parameter when your routing rules contain empty String values ("") as seen in the example above.
    """
    websiteDomain: Optional[str] = None
    """
    Domain of the website endpoint. This is used to create Route 53 alias records.
    """
    websiteEndpoint: Optional[str] = None
    """
    Website endpoint.
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


class BucketWebsiteConfiguration(BaseModel):
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
    BucketWebsiteConfigurationSpec defines the desired state of BucketWebsiteConfiguration
    """
    status: Optional[Status] = None
    """
    BucketWebsiteConfigurationStatus defines the observed state of BucketWebsiteConfiguration.
    """


class BucketWebsiteConfigurationList(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    items: List[BucketWebsiteConfiguration]
    """
    List of bucketwebsiteconfigurations. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ListMeta] = None
    """
    Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """