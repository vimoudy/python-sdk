# DashboardBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Id | [optional] 
**user_id** | **int** | Id of User | [optional] 
**title** | **str** | Look Title | [optional] 
**description** | **str** | Description | [optional] 
**readonly** | **bool** | Is Read-only | [optional] 
**hidden** | **bool** | Is Hidden | [optional] 
**refresh_interval** | **str** | Refresh Interval | [optional] 
**refresh_interval_to_i** | **int** | Refresh Interval as Integer | [optional] 
**space** | [**SpaceBase**](SpaceBase.md) | Space | [optional] 
**model** | [**LookModel**](LookModel.md) | Model | [optional] 
**content_favorite_id** | **int** | Content Favorite Id | [optional] 
**scheduled_plan** | [**ScheduledPlan**](ScheduledPlan.md) | ScheduledPlan | [optional] 
**content_metadata_id** | **int** | Id of content metadata | [optional] 
**query_timezone** | **str** | Timezone in which the Dashboard will run by default. | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


