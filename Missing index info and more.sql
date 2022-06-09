--------------------------------------------------------------------
-- Looking at filegroups and files structures? Run this script -----
--------------------------------------------------------------------
SELECT	f.name
		,f.file_id
		,f.physical_name
		,fg.name
		,fg.is_default
		,TotalSizeMB = CONVERT(DECIMAL(15, 2), f.size / 128.0)
		,SpaceUsedMB = CONVERT(DECIMAL(15,2), FILEPROPERTY(f.name, 'SpaceUsed') / 128.0)
		,Growth = CASE f.is_percent_growth
			WHEN 1 THEN f.growth
			ELSE CONVERT(DECIMAL(15, 2), f.growth /128.0)
			END
		,f.is_percent_growth
FROM	sys.database_files f
	LEFT JOIN sys.data_spaces fg ON f.data_space_id = fg.data_space_id;

-----------------------------------------------------------------------
------------ Looking for missing indexes? Run this script -------------
-----------------------------------------------------------------------
SELECT DISTINCT
	mid.statement
	,mid.equality_columns
	,mid.included_columns
	,migs.unique_compiles
	,migs.user_seeks
	,migs.avg_total_user_cost
	,migs.avg_user_impact
	,ObjectName = OBJECT_NAME(mid.[object_id])
	,p.rows
	,migs.last_user_seek
FROM	sys.dm_db_missing_index_group_stats migs
	JOIN sys.dm_db_missing_index_groups mig ON migs.group_handle = mig.index_group_handle
	JOIN sys.dm_db_missing_index_details mid ON mig.index_handle = mid.index_handle
	JOIN sys.partitions p ON p.[object_id] = mid.[object_id];

