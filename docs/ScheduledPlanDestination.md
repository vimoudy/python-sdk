# ScheduledPlanDestination

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**scheduled_plan_id** | **int** | Id of a scheduled plan you own | [optional] 
**format** | **str** | Format requested by the given destination (i.e. PDF, etc.) | [optional] 
**apply_formatting** | **bool** | Are values formatted? (containing currency symbols, digit separators, etc. | [optional] 
**apply_vis** | **bool** | Whether visualization options are applied to the results. | [optional] 
**address** | **str** | Address for recipient. For email e.g. &#39;user@example.com&#39;. For webhooks e.g. &#39;https://domain/path&#39;. For Amazon S3 e.g. &#39;s3://bucket-name/path/&#39;. For SFTP e.g. &#39;sftp://host-name/path/&#39;.  | [optional] 
**looker_recipient** | **bool** | Whether the recipient is a Looker user on the current instance (only applicable for email recipients) | [optional] 
**type** | **str** | Type of the address (&#39;email&#39;, &#39;webhook&#39;, &#39;s3&#39;, or &#39;sftp&#39;) | [optional] 
**parameters** | **str** | JSON object containing parameters for external scheduling. For Amazon S3, this requires keys and values for access_key_id and region. For SFTP, this requires a key and value for username. | [optional] 
**secret_parameters** | **str** | (Write-Only) JSON object containing secret parameters for external scheduling. For Amazon S3, this requires a key and value for secret_access_key. For SFTP, this requires a key and value for password. | [optional] 
**message** | **str** | Optional message to be included in scheduled emails | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


