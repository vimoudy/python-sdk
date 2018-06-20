# RunningQueries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**user** | [**UserPublic**](UserPublic.md) | User who initiated the query | [optional] 
**query** | [**Query**](Query.md) | Query that was run | [optional] 
**sql_query** | [**SqlQuery**](SqlQuery.md) | SQL Query that was run | [optional] 
**look** | [**LookBasic**](LookBasic.md) | Look of query that was run | [optional] 
**created_at** | **str** | Date/Time Query was initiated | [optional] 
**completed_at** | **str** | Date/Time Query was completed | [optional] 
**query_id** | **str** | Query Id | [optional] 
**source** | **str** | Source (look, dashboard, queryrunner, explore, etc.) | [optional] 
**node_id** | **str** | Node Id | [optional] 
**slug** | **str** | Slug | [optional] 
**query_task_id** | **str** | ID of a Query Task | [optional] 
**cache_key** | **str** | Cache Key | [optional] 
**connection_name** | **str** | Connection | [optional] 
**dialect** | **str** | Dialect | [optional] 
**connection_id** | **str** | Connection ID | [optional] 
**message** | **str** | Additional Information(Error message or verbose status) | [optional] 
**status** | **str** | Status description | [optional] 
**runtime** | **float** | Number of seconds elapsed running the Query | [optional] 
**sql** | **str** | SQL text of the query as run | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


