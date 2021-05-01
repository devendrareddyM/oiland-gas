"""
Graph data
"""

login_query = """SELECT * FROM public.users where email_id='{email_id}' and password='{password}'"""

coke_drum_actual_values = """select * from plant_coke_drum where type=True and timestamp=(select max(timestamp) 
from plant_coke_drum where version={version} and type=true) and version={version}"""
coke_drum_predicted_values = """select * from plant_coke_drum where type=True and timestamp=(select max(timestamp) 
from plant_coke_drum where version={version} and type=True) and version={version} """
# coke_drum_yields_actual_values = """select * from coke_drum_yields where type= False and timestamp=(select max(
# timestamp) from coke_drum_yields) """
#
# coke_drum_yields_predicted_values = """select * from coke_drum_yields where type=True and timestamp=(select max(
# timestamp) from coke_drum_yields) """

feed_actual_values = """select * from plant_feed_data where type=False and timestamp=(select max(timestamp) from 
plant_feed_data where type=False and version={version}) and version={version}"""
feed_predicted_values = """select * from plant_feed_data where type=True and timestamp=(select max(timestamp) 
from plant_feed_data where version={version} and type=true) and version={version} """
# feed_yields_actual_values = """select * from feed_data_yields where type= False and timestamp=(select max(
# timestamp) from feed_data_yields) """
#
# feed_yields_predicted_values = """select * from feed_data_yields where type=True and timestamp=(select max(
# timestamp) from feed_data_yields) """
heater_actual_values = """select * from plant_heater where type=False and timestamp=(select max(timestamp) from 
plant_heater where type=false and version={version}) and version={version} """
heater_predicted_values = """select * from plant_heater where type=True and timestamp=(select max(timestamp) 
from plant_heater where version={version} and type=true) and version={version} """
# heater_yields_actual_values = """select * from heater_yields where type= False and timestamp=(select max(
# timestamp) from heater_yields) """
#
# heater_yields_predicted_values = """select * from heater_yields where type=True and timestamp=(select max(
# timestamp) from heater_yields) """
fractinator_actual_values = """select * from plant_fractinator where type=False and timestamp=(select max(timestamp) from 
plant_fractinator where type=false and version={version}) and version={version}"""
fractinator_predicted_values = """select * from plant_fractinator where type=True and timestamp=(select max(timestamp) 
from plant_fractinator where version={version} and type=true) and version={version} """
# fractinator_yields_actual_values = """select * from fractinator_yields where type= False and timestamp=(select max(
# timestamp) from fractinator_yields) """
#
# fractinator_yields_predicted_values = """select * from fractinator_yields where type=True and timestamp=(select max(
# timestamp) from fractinator_yields) """

# coke_drum_yields_actual_values_graph = """select process_value as actual_value, timestamp,uom from coke_drum_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=False"""
# coke_drum_yields_predicted_values_graph = """select process_value as predicted_value, timestamp from coke_drum_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=True """
#
# feed_yields_actual_values_graph = """select process_value as actual_value,timestamp from feed_data_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=False """
# feed_yields_predicted_values_graph = """select process_value as predicted_value,timestamp,uom from feed_data_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=True """
#
# heater_yields_predicted_values_graph = """select process_value as predicted_value,timestamp,uom from heater_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=True"""
# heater_yields_actual_values_graph = """select process_value as actual_value,timestamp from heater_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=False"""
#
# fractinator_yields_actual_values_graph = """select process_value as actual_value,timestamp from fractinator_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=False"""
# fractinator_yields_predicted_values_graph = """select process_value as predicted_value,timestamp,uom from fractinator_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=True"""

update_predict_values = """UPDATE {table_name} SET  min_value={min_value}, max_value={max_value} WHERE 
parameter='{parameter}' and timestamp=(select max(timestamp) from {table_name} where version={version} and type=True) and type=True;"""
update_yields_predict_values = """UPDATE {table_name} SET  min_value={min_value}, max_value={max_value} WHERE 
parameter='{parameter}' and timestamp=(select max(timestamp) from {table_name}) and type=True;"""

get_predicted_version_data = """select parameter,min_value,max_value,uom,type,version from {table_name} where 
type=True and version={version}"""
update_config_predict_values = """UPDATE {table_name} SET  min_value={min_value}, max_value={max_value} WHERE 
parameter='{parameter}' and type=true and version={version}; """
get_version_number = """Select MAX(version) FROM public.{table_name}"""
insert_predicted_values = """INSERT INTO public.{table_name}(equipment_id, process_id, parameter,max_value, 
min_value, "timestamp", uom, type,version)VALUES ({equipment_id}, {process_id},'{parameter}',{max_value},{min_value},'{timestamp}',
'{uom}', true,{version}); """

get_predicted_version_list = """ select distinct version from {table_name} where type=true order by version """

# dcu_yields_actual_values_graph = """select process_value as actual_value, timestamp,uom,parameter from dcu_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=False"""
# dcu_yields_predicted_values_graph = """select process_value as predicted_value, timestamp,parameter from dcu_yields where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' and type=True"""

dcu_yields_actual_values = """select * from dcu_yields where type=False and timestamp=(select max(timestamp) from 
dcu_yields where version={version} and type=False) and version={version} """

dcu_yields_predicted_values = """select * from dcu_yields where type=True and timestamp=(select max(timestamp) from 
dcu_yields where version={version} and type=True) and version={version} """

insert_actual_values = """INSERT INTO public.{table_name}(equipment_id, process_id, parameter,max_value,min_value, "timestamp", uom, type,version,process_value)VALUES ({equipment_id}, {process_id},'{parameter}',{max_value},{min_value},'{timestamp}','{uom}', false,{version},{process_value}); """

coke_yields_graph = """select timestamp,coke_yields,predicted_coke_yields from plant_coke_yields where timestamp 
between '{start_date}' and '{end_date}' """

coke_yields_actual_predicted_values = """select coke_yields,predicted_coke_yields from plant_coke_yields where timestamp=(select max(timestamp) from plant_coke_yields)"""

""" ************************* UPDATED DESIGN QUERIES **********************************************"""
# coke_actual_values = """select I.timestamp,I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where timestamp=(select max(timestamp)
# from parameter_input) and feed_type='coke_drum' order by S.psn_id"""

coke_actual_values = """select I.parameter,S.unit,S.sh_name,Round(avg(I.parameter_value),3) as parameter_value,Round(avg(para_val_percent),3) as actual_percent_value from 
parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='coke_drum' group by I.parameter,S.unit,S.sh_name,S.psn_id order by S.psn_id"""

# input_feed_data = """select I.timestamp,I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where timestamp=(select max(timestamp)
# from parameter_input) and feed_type='input_feed' order by S.psn_id """


# input_feed_data = """select I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='input_feed' and I.value_type='average' order by S.psn_id """
input_feed_data = """select I.parameter,S.unit,S.sh_name,Round(avg(I.parameter_value),3) as parameter_value,Round(avg(para_val_percent),3) as actual_percent_value from 
parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='input_feed' group by I.parameter,S.unit,S.sh_name,S.psn_id order by S.psn_id"""
# heater_actual_data_values = """select I.timestamp,I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where timestamp=(select max(timestamp)
# from parameter_input) and feed_type='heater' order by S.psn_id"""
# heater_actual_data_values = """select I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='heater' and I.value_type='average' order by S.psn_id"""
heater_actual_data_values = """select I.parameter,S.unit,S.sh_name,Round(avg(I.parameter_value),3) as parameter_value,Round(avg(para_val_percent),3) as actual_percent_value from 
parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='heater' group by I.parameter,S.unit,S.sh_name,S.psn_id order by S.psn_id"""

#
# fractinator_actual_data_values = """select I.timestamp,I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where timestamp=(select max(timestamp)
# from parameter_input) and feed_type='fractinator' order by S.psn_id """

# fractinator_actual_data_values = """select I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='fractinator' and I.value_type='average' order by S.psn_id """
fractinator_actual_data_values = """select I.parameter,S.unit,S.sh_name,Round(avg(I.parameter_value),3) as parameter_value,Round(avg(para_val_percent),3) as actual_percent_value from 
parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='fractinator' group by I.parameter,S.unit,S.sh_name,S.psn_id order by S.psn_id"""

# dcu_yields_actual_data_values = """select I.timestamp,I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where timestamp=(select max(timestamp)
# from parameter_input) and feed_type='dcu_actual' order by S.psn_id"""
# dcu_yields_actual_data_values = """select I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='dcu_actual' and I.value_type='average' order by S.psn_id"""
dcu_yields_actual_data_values = """select I.parameter,S.unit,S.sh_name,Round(avg(I.parameter_value),3) as parameter_value,Round(avg(para_val_percent),3) as actual_percent_value from 
parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='dcu_actual' group by I.parameter,S.unit,S.sh_name,S.psn_id order by S.psn_id"""

coke_predicted_values = """select S.parameter_name,I.rec_value as parameter_value,S.unit,S.sh_name from 
public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='coke_drum' order by S.psn_id"""
input_feed_pred_data = """select S.parameter_name,I.rec_value as parameter_value,S.unit,S.sh_name from 
public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='input_feed' order by S.psn_id"""

heater_pred_data_values = """select S.parameter_name,I.rec_value as parameter_value,S.unit,S.sh_name from 
public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='heater' order by S.psn_id"""
fractinator_pred_data_values = """select S.parameter_name,I.rec_value as parameter_value,S.unit,S.sh_name from 
public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='fractinator' order by S.psn_id"""
# dcu_yields_result_data = """select S.parameter_name,I.rec_value as parameter_value,S.unit,S.sh_name from
# public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='dcu_actual' order by S.psn_id"""
dcu_yields_result_data = """select S.parameter_name,ROUND(((select rec_value from public.recommendation_tbl where param_name='sfbl')*(select rec_value from public.recommendation_tbl where param_name='fu')/100),4)
			 as parameter_value,S.unit,S.sh_name from recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='dcu_actual' and param_name='sfbl'
			 
UNION ALL
select S.parameter_name,ROUND(((select rec_value from public.recommendation_tbl where param_name='lpg')*(select rec_value from public.recommendation_tbl where param_name='fu')/100),4)
			 as parameter_value,S.unit,S.sh_name from recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='dcu_actual' and param_name='lpg'

UNION ALL
select S.parameter_name,ROUND(((select rec_value from public.recommendation_tbl where param_name='lcn')*(select rec_value from public.recommendation_tbl where param_name='fu')/100),4)
			 as parameter_value,S.unit,S.sh_name from recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='dcu_actual' and param_name='lcn'			 
UNION ALL
select S.parameter_name,ROUND(((select rec_value from public.recommendation_tbl where param_name='hcn')*(select rec_value from public.recommendation_tbl where param_name='fu')/100),4)
			 as parameter_value,S.unit,S.sh_name from recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='dcu_actual' and param_name='hcn'			 

UNION ALL
select S.parameter_name,ROUND(((select rec_value from public.recommendation_tbl where param_name='lcgo')*(select rec_value from public.recommendation_tbl where param_name='fu')/100),4)
			 as parameter_value,S.unit,S.sh_name from recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='dcu_actual' and param_name='lcgo'			 

UNION ALL
select S.parameter_name,ROUND(((select rec_value from public.recommendation_tbl where param_name='hcgo')*(select rec_value from public.recommendation_tbl where param_name='fu')/100),4)
			 as parameter_value,S.unit,S.sh_name from recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type='dcu_actual' and param_name='hcgo'			 
	"""
dcu_yields_actual_values_graph = """select parameter,parameter_value as actual_value,para_val_percent as actual_percent_value,timestamp from 
parameter_input where parameter ='{parameter}' and timestamp between '{start_date}' and '{end_date}' order by timestamp"""
dcu_yields_predicted_values_graph = """select I.rec_value as predicted_value from 
public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where S.parameter_name='{parameter}'"""

insert_actual_data = """INSERT INTO public.report_input_parameter("timestamp", parameter, parameter_value, 
unit,value_type,"current_ts") VALUES ('{timestamp}', '{parameter}',{parameter_value},'{unit}','actual','{current_ts}'); """
insert_predicted_data = """
INSERT INTO public.report_recommendation_tbl("timestamp", parameter, parameter_value, 
unit,value_type,"current_ts") VALUES ('{timestamp}', '{parameter}',{parameter_value},'{unit}','rec','{current_ts}'); """

# coke_yields_actual_values = """SELECT ROUND(
#   100.0 * (
#       (select I.parameter_value from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where timestamp=(select max(timestamp)
# from parameter_input) and feed_type='coke' order by S.psn_id)/ (select I.parameter_value from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where timestamp=(select max(timestamp)
# from parameter_input) and I.parameter='Feed_to_the_unit' order by S.psn_id)
#   ), 1) AS coke_yields
# FROM parameter_input limit 1"""
# coke_yields_actual_values = """select I.parameter,I.parameter_value as coke_yields,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where feed_type='coke' and I.value_type='coke_yield' order by S.psn_id"""
coke_yields_actual_values = """
SELECT P.parameter,S.sh_name,S.unit,ROUND(((avg(P.parameter_value)/avg(I.parameter_value))*100),4) as coke_yields
FROM parameter_input P
JOIN parameter_input I  ON P.timestamp=I.timestamp join parameter_sh_name S on P.parameter= S.parameter_name
WHERE S.feed_type='coke'
AND I.parameter= 'Feed_to_the_unit' group by P.parameter,S.sh_name,S.unit"""
#
# coke_yields_predicted_values = """SELECT ROUND(
#   100.0 * (
#       (select I.rec_value from
# public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where S.parameter_name='Coke' order by S.psn_id)/ (select I.rec_value from
# public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where S.parameter_name='Feed_to_the_unit' order by S.psn_id)), 1) AS recommended_coke_yields
# FROM public.recommendation_tbl limit 1"""
#
# coke_yields_forecast_result = """select fc_val AS pre_recommended_coke_yields from public.forecast_result where
# commodity='coke' and fc_dt=(select max(timestamp)from parameter_input) and dw='{dw}' """

coke_yields_forecast_result = """select fc_val AS pre_recommended_coke_yields from public.forecast_result where 
commodity='coke' and fc_dt=(select min(fc_dt) from forecast_result where dw='{dw}' and period='Daily' and commodity='coke') and dw='{dw}' and period='Daily'
"""
# coke_yields_post_rec_forecast_values = """select fc_val AS pre_recommended_coke_yields from public.forecast_result where
# commodity='coke' and fc_dt=(select max(fc_dt)from forecast_result where dw='{dw}' and period='Daily' and commodity='coke') and dw='{dw}' and period='Daily'
# """
coke_yields_post_rec_forecast_values = """
select fc_val AS pre_recommended_coke_yields from public.forecast_result where 
commodity='coke' and fc_dt=(select max(timestamp)from parameter_input) and dw='{dw}' and period='Daily'"""
# weekly_coke_yields_forecast_result = """select fc_val AS pre_recommended_coke_yields from public.forecast_result where
# commodity='coke' and fc_dt=(select max(timestamp)from parameter_input)+interval '7 day' and dw='{dw}'"""

weekly_coke_yields_forecast_result = """select fc_val AS pre_recommended_coke_yields from public.forecast_result where 
commodity='coke' and fc_dt=(select max(fc_dt)from forecast_result where dw='{dw}' and period='Weekly') and dw='{dw}' and period='Weekly'
"""
weekly_coke_yields_post_rec_forecast_result = """select fc_val AS pre_recommended_coke_yields from public.forecast_result where 
commodity='coke' and fc_dt=(select max(fc_dt)from forecast_result where dw='{dw}' and period='Weekly' and dw='{dw}') and dw='{dw}' and period='Weekly'
"""

# coke_yields_forecast_pre_post_result = """select fc_val AS parameter_value,fc_dt as timestamp from forecast_result where fc_dt between '{start_date}' and '{end_date}' and commodity='coke' and dw='{dw}' order by fc_dt asc
# """
coke_yields_forecast_pre_post_result = """select fc_val AS parameter_value,fc_dt as timestamp from forecast_result where commodity='coke' and dw='{dw}' and period='{period}' order by fc_dt asc"""

# pie_dcu_actual_yields = """select I.timestamp,I.parameter,I.parameter_value,S.unit,S.sh_name from
# parameter_input I join parameter_sh_name S on S.parameter_name=I.parameter where timestamp=(select max(timestamp)
# from parameter_input) and feed_type in ('dcu_actual','coke') order by S.psn_id"""

# pie_dcu_actual_yields = """SELECT DISTINCT ON (P.timestamp) P.timestamp,P.parameter,S.sh_name,S.unit, ROUND(((P.parameter_value/I.parameter_value)*100),5) as parameter_value
# FROM parameter_input P
# JOIN parameter_input I  ON P.timestamp=I.timestamp join parameter_sh_name S on P.parameter= S.parameter_name
# WHERE P.parameter in ('Sweet_FG_to_Battery_limit') and P.timestamp =(select max(timestamp) from parameter_input)
# AND I.parameter= 'Feed_to_the_unit' and I.timestamp=(select max(timestamp) from parameter_input)
# UNION ALL
# SELECT DISTINCT ON (P.timestamp) P.timestamp,P.parameter,S.sh_name,S.unit, ROUND(((P.parameter_value/I.parameter_value)*100),5) as parameter_value
# FROM parameter_input P
# JOIN parameter_input I  ON P.timestamp=I.timestamp join parameter_sh_name S on P.parameter= S.parameter_name
# WHERE P.parameter in ('Sweet_LPG') and P.timestamp =(select max(timestamp) from parameter_input)
# AND I.parameter= 'Feed_to_the_unit' and I.timestamp=(select max(timestamp) from parameter_input)
# UNION ALL
# SELECT DISTINCT ON (P.timestamp) P.timestamp,P.parameter,S.sh_name,S.unit, ROUND(((P.parameter_value/I.parameter_value)*100),5) as parameter_value
# FROM parameter_input P
# JOIN parameter_input I  ON P.timestamp=I.timestamp join parameter_sh_name S on P.parameter= S.parameter_name
# WHERE P.parameter in ('Total_LCN') and P.timestamp =(select max(timestamp) from parameter_input)
# AND I.parameter= 'Feed_to_the_unit' and I.timestamp=(select max(timestamp) from parameter_input)
# UNION ALL
# SELECT DISTINCT ON (P.timestamp) P.timestamp,P.parameter,S.sh_name,S.unit, ROUND(((P.parameter_value/I.parameter_value)*100),5) as parameter_value
# FROM parameter_input P
# JOIN parameter_input I  ON P.timestamp=I.timestamp join parameter_sh_name S on P.parameter= S.parameter_name
# WHERE P.parameter in ('Total_HCN') and P.timestamp =(select max(timestamp) from parameter_input)
# AND I.parameter= 'Feed_to_the_unit' and I.timestamp=(select max(timestamp) from parameter_input)
# UNION ALL
# SELECT DISTINCT ON (P.timestamp) P.timestamp,P.parameter,S.sh_name,S.unit, ROUND(((P.parameter_value/I.parameter_value)*100),5) as parameter_value
# FROM parameter_input P
# JOIN parameter_input I  ON P.timestamp=I.timestamp join parameter_sh_name S on P.parameter= S.parameter_name
# WHERE P.parameter in ('Total_LCGO') and P.timestamp =(select max(timestamp) from parameter_input)
# AND I.parameter= 'Feed_to_the_unit' and I.timestamp=(select max(timestamp) from parameter_input)
# UNION ALL
# SELECT DISTINCT ON (P.timestamp) P.timestamp,P.parameter,S.sh_name,S.unit, ROUND(((P.parameter_value/I.parameter_value)*100),5) as parameter_value
# FROM parameter_input P
# JOIN parameter_input I  ON P.timestamp=I.timestamp join parameter_sh_name S on P.parameter= S.parameter_name
# WHERE P.parameter in ('Total_HCGO') and P.timestamp =(select max(timestamp) from parameter_input)
# AND I.parameter= 'Feed_to_the_unit' and I.timestamp=(select max(timestamp) from parameter_input)
# UNION ALL
# SELECT DISTINCT ON (P.timestamp) P.timestamp,P.parameter,S.sh_name,S.unit, ROUND(((P.parameter_value/I.parameter_value)*100),5) as parameter_value
# FROM parameter_input P
# JOIN parameter_input I  ON P.timestamp=I.timestamp join parameter_sh_name S on P.parameter= S.parameter_name
# WHERE P.parameter in ('Coke') and P.timestamp =(select max(timestamp) from parameter_input)
# AND I.parameter= 'Feed_to_the_unit' and I.timestamp=(select max(timestamp) from parameter_input)"""
#
#
pie_dcu_actual_yields = """
SELECT P.parameter,S.sh_name,S.unit,ROUND(((avg(P.parameter_value)/avg(I.parameter_value))*100),4) as parameter_value
FROM parameter_input P
JOIN parameter_input I  ON P.timestamp=I.timestamp join parameter_sh_name S on P.parameter= S.parameter_name
WHERE P.parameter in ('Sweet_FG_to_Battery_limit','Sweet_LPG','Total_LCN','Total_HCN','Total_LCGO','Total_HCGO','Coke')
AND I.parameter= 'Feed_to_the_unit' group by P.parameter,S.sh_name,S.unit,S.psn_id order by S.psn_id"""

# pie_dcu_predicted_yields = """select I.fc_dt as timestamp,S.parameter_name as parameter,I.fc_val as parameter_value,S.unit,S.sh_name from
# forecast_result I join parameter_sh_name S on S.sh_name=I.commodity where I.fc_dt=(select max(fc_dt)
# from forecast_result) and feed_type in ('dcu_actual','coke','dcu_recomnd') order by S.psn_id"""

pie_dcu_predicted_yields = """select S.parameter_name as parameter,I.fc_val as parameter_value,S.unit,S.sh_name from 
forecast_result I join parameter_sh_name S on S.sh_name=I.commodity where I.fc_dt=(select min(fc_dt) from forecast_result where dw='Pre_Rec' and period='Daily' and commodity = 'coke') and period='Daily' and dw='Pre_Rec' and feed_type in ('dcu_actual','coke','dcu_recomnd') order by S.psn_id"""

pie_dcu_recommended_yields = """select S.parameter_name,I.rec_value as parameter_value,S.unit,S.sh_name from 
public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type in ('dcu_actual','coke') order by S.psn_id"""

pie_dcu_recommended_other_yields = """select S.parameter_name,I.rec_value as parameter_value,S.unit,S.sh_name from 
public.recommendation_tbl I join parameter_sh_name S on S.sh_name=I.param_name where feed_type in ('input_feed','heater','fractinator','coke_drum') order by S.psn_id"""

# predicted_parameters_graph_data = """SELECT json_build_object(
#     'Sweet_FG_to_Battery_limit', (SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
# 	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Sweet_FG_to_Battery_limit' and fc_dt between '{start_date}' and '{end_date}' and dw='{dw}'),
# 	'Sweet_LPG',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
# 	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Sweet_LPG' and fc_dt between '{start_date}' and '{end_date}' and dw='{dw}'),
# 	'LCN',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
# 	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Total_LCN' and fc_dt between '{start_date}' and '{end_date}' and dw='{dw}'),
# 	'HCN',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
# 	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Total_HCN' and fc_dt between '{start_date}' and '{end_date}' and dw='{dw}'),
# 	'LCGO',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
# 	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Total_LCGO' and fc_dt between '{start_date}' and '{end_date}' and dw='{dw}'),
# 	'HCGO',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
# 	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Total_HCGO' and fc_dt between '{start_date}' and '{end_date}' and dw='{dw}'),
# 	'Coke',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
# 	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Coke' and fc_dt between '{start_date}' and '{end_date}' and dw='{dw}')
# )"""
predicted_parameters_graph_data = """SELECT json_build_object('Sweet_FG_to_Battery_limit', (SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Sweet_FG_to_Battery_limit'and dw='{dw}' and period='{period}'),
	'Sweet_LPG',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Sweet_LPG' and dw='{dw}' and period='{period}'),
	'LCN',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Total_LCN' and dw='{dw}' and period='{period}'),
	'HCN',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Total_HCN' and dw='{dw}' and period='{period}'),
	'LCGO',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Total_LCGO' and dw='{dw}' and period='{period}'),
	'HCGO',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Total_HCGO' and dw='{dw}' and period='{period}'),
	'Coke',(SELECT json_agg(json_build_object('predicted_value',fc_val,'timestamp',fc_dt,'unit',PS.unit))
	from forecast_result FR join public.parameter_sh_name PS on FR.commodity=PS.sh_name where PS.parameter_name='Coke' and dw='{dw}' and period='{period}'))"""

actual_predicted_st_end_date = """SELECT json_build_object(
'max_timestamp',H.maxtm,
'min_timestamp',H.mintm
) 
FROM
(select max(timestamp) as maxtm,min(timestamp) as mintm FROM public.parameter_input)as H 
UNION ALL
SELECT json_build_object(
'max_timestamp',P.maxtm,
'min_timestamp',P.mintm
) 
FROM
(select max(fc_dt) as maxtm,min(fc_dt) as mintm FROM public.forecast_result where dw='Post_Rec')as P
UNION ALL
SELECT json_build_object(
'max_timestamp',R.maxtm,
'min_timestamp',R.mintm
) 
FROM
(select max(fc_dt) as maxtm,min(fc_dt) as mintm FROM public.forecast_result where dw='Pre_Rec')as R"""

update_parameter_input_status_query = """update parameter_input set status=true"""

actual_yields_graph_data_in_percent = """
SELECT DISTINCT ON (P.timestamp) P.timestamp,extract(epoch from P.timestamp) as epoch_time,P.parameter, ROUND(((P.parameter_value/I.parameter_value)*100),5) as actual_value
FROM parameter_input P
JOIN parameter_input I  ON P.timestamp=I.timestamp
WHERE P.parameter ='{parameter}' and P.timestamp between '{st_date}'  and  '{end_date}'
AND I.parameter= 'Feed_to_the_unit' and I.timestamp between '{st_date}'  and  '{end_date}' order by P.timestamp;"""

#
# GET_FURNACE_RUN_DA = """select extract(epoch from t1.obs_time) as epoch_time, t1.obs_time, t1.run, t1.run_hours, t1.efrz1, t2.efrz2, t3.efrz3, t4.dsrz1, t5.dsrz2, t6.dsrz3, t7.cprz1, t8.cprz2, t9.cprz3,
# t10.shcz1, t11.shcz2, t12.shcz3, t13.tmtz1, t14.tmtz2, t15.tmtz3, t16.cotz1, t17.cotz2, t18.cotz3, t19.dosage
# from
# 	(select obs_time, run, run_hours, pro_val efrz1
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 		join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
# 	where tm.param_key =1 and zd.zone_key =1) t1
#
# 		join (select pro_val efrz2, pt.obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =1 and zd.zone_key =2) t2
# 		on t1.obs_time = t2.obs_time
# 		join (select pro_val efrz3, obs_time
# 	from public.process_tags pt3
# 		join tag_map tm on tm.map_key = pt3.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =1 and zd.zone_key =3) t3
# 		on t2.obs_time = t3.obs_time
# 		join (select pro_val dsrz1, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =2 and zd.zone_key =1) t4
# 		on t1.obs_time = t4.obs_time
# 		join (select pro_val dsrz2, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =2 and zd.zone_key =2) t5
# 		on t1.obs_time = t5.obs_time
# 		join (select pro_val dsrz3, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =2 and zd.zone_key =3) t6
# 		on t1.obs_time = t6.obs_time
# 		join (select pro_val cprz1, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =7 and zd.zone_key =1) t7
# 		on t1.obs_time = t7.obs_time
# 		join (select pro_val cprz2, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =7 and zd.zone_key =2) t8
# 		on t1.obs_time = t8.obs_time
# 		join (select pro_val cprz3, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =7 and zd.zone_key =3) t9
# 		on t1.obs_time = t9.obs_time
#
# 		join (select pro_val shcz1, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =3 and zd.zone_key =1) t10
# 		on t1.obs_time = t10.obs_time
#
# 		join (select pro_val shcz2, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =3 and zd.zone_key =2) t11
# 		on t1.obs_time = t11.obs_time
#
# 		join (select pro_val shcz3, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =3 and zd.zone_key =3) t12
# 		on t1.obs_time = t12.obs_time
#
# 		join (select pro_val tmtz1, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =8 and zd.zone_key =1) t13
# 		on t1.obs_time = t13.obs_time
#
# 		join (select pro_val tmtz2, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =8 and zd.zone_key =2) t14
# 		on t1.obs_time = t14.obs_time
#
# 		join (select pro_val tmtz3, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =8 and zd.zone_key =3) t15
# 		on t1.obs_time = t15.obs_time
#
# 		join (select pro_val cotz1, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =6 and zd.zone_key =1) t16
# 		on t1.obs_time = t16.obs_time
#
# 		join (select pro_val cotz2, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =6 and zd.zone_key =2) t17
# 		on t1.obs_time = t17.obs_time
#
# 		join (select pro_val cotz3, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =6 and zd.zone_key =3) t18
# 		on t1.obs_time = t18.obs_time
#
# 		join (select pro_val dosage, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =28) t19
# 		on t1.obs_time = t19.obs_time;"""

GET_ZONE_WISE_DATA = '''select extract(epoch from obs_time) as epoch_time, obs_time, ed.eq_name,  zd.zone_name , pcd.param_cat_name, td.tag_name, td.tag_short_name, pt.pro_val from public.param_cat_dim pcd
join public.tag_map tm on tm.param_cat_key =pcd.param_cat_key
join public.tag_dim td on td.tag_key = tm.tag_key
join public.zone_dim zd on zd.zone_key = tm.zone_key
join public.equipment_dim ed on ed.eq_key = tm.eq_key
join public.process_tags pt on pt.map_key =tm.map_key;'''

GET_FURNACE_RUN_DATA = '''select timestamp,image,prediction_result from vision_result_table '''

vision_insert="""INSERT INTO public.vision_input_table(
	"timestamp", image, overheated)
	VALUES (now(),'{image}','{over}');"""

FRL_GRAPH = """SELECT json_build_object('Zone', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp', extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val, 'uom',pd.uom))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name = '{parameter_tag}' and zd.zone_name='{Zone}' and run={run}))"""

# FRL_GRAPH = """SELECT json_build_object('Zone', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp', extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val, 'uom',pd.uom))

# from process_tags pt
# join tag_map tm on tm.map_key = pt.map_key
# join zone_dim zd on zd.zone_key =tm.zone_key
# join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
# join parameter_dim pm on tm.param_key=pm.param_key
# join parameter_dim pd on pd.param_key=tm.param_key
# where tm.param_key =1 and zd.zone_key =1 and run=1 and
# tm.param_key =6 and zd.zone_key =1 and run=1 and
# tm.param_key =7 and zd.zone_key =1 and run=1 and
# tm.param_key =8 and zd.zone_key =1 and run=1))"""

GET_FRL_ACTUAL_DATA = """select extract(epoch from t1.obs_time) as epoch_time, t1.obs_time, t1.run, t1.run_hours, t1.efrz1, t2.efrz2, t3.efrz3, t4.dsrz1, t5.dsrz2, t6.dsrz3, t7.cprz1, t8.cprz2, t9.cprz3,
t10.shcz1, t11.shcz2, t12.shcz3, t13.tmtz1, t14.tmtz2, t15.tmtz3, t16.cotz1, t17.cotz2, t18.cotz3, t19.dosage,
t20.fuelflwz1, t21.fuelflwz2, t22.fuelflwz3, t23.fuelwallz1, t24.fuelwallz2, t25.fuelwallz3, 
(t20.fuelflwz1+t23.fuelwallz1) as Tot_fuel_wall_z1, 
(t21.fuelflwz2+t24.fuelwallz2) as Tot_fuel_wall_z2, 
(t22.fuelflwz3+t25.fuelwallz3) as Tot_fuel_wall_z3

from 
	(select obs_time, run, run_hours, pro_val efrz1
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
		join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
	where tm.param_key =1 and zd.zone_key =1) t1

		join (select pro_val efrz2,  pt.obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =1 and zd.zone_key =2) t2
		on t1.obs_time = t2.obs_time
		join (select pro_val efrz3, obs_time
	from public.process_tags pt3
		join tag_map tm on tm.map_key = pt3.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =1 and zd.zone_key =3) t3
		on t2.obs_time = t3.obs_time
		join (select pro_val dsrz1, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =2 and zd.zone_key =1) t4
		on t1.obs_time = t4.obs_time
		join (select pro_val dsrz2, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =2 and zd.zone_key =2) t5
		on t1.obs_time = t5.obs_time
		join (select pro_val dsrz3, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =2 and zd.zone_key =3) t6
		on t1.obs_time = t6.obs_time
		join (select pro_val cprz1, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =7 and zd.zone_key =1) t7
		on t1.obs_time = t7.obs_time
		join (select pro_val cprz2, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =7 and zd.zone_key =2) t8
		on t1.obs_time = t8.obs_time
		join (select pro_val cprz3, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =7 and zd.zone_key =3) t9
		on t1.obs_time = t9.obs_time

		join (select pro_val shcz1, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =3 and zd.zone_key =1) t10
		on t1.obs_time = t10.obs_time

		join (select pro_val shcz2, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =3 and zd.zone_key =2) t11
		on t1.obs_time = t11.obs_time

		join (select pro_val shcz3, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =3 and zd.zone_key =3) t12
		on t1.obs_time = t12.obs_time

		join (select pro_val tmtz1, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =8 and zd.zone_key =1) t13
		on t1.obs_time = t13.obs_time

		join (select pro_val tmtz2, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =8 and zd.zone_key =2) t14
		on t1.obs_time = t14.obs_time

		join (select pro_val tmtz3, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =8 and zd.zone_key =3) t15
		on t1.obs_time = t15.obs_time

		join (select pro_val cotz1, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =6 and zd.zone_key =1) t16
		on t1.obs_time = t16.obs_time

		join (select pro_val cotz2, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =6 and zd.zone_key =2) t17
		on t1.obs_time = t17.obs_time

		join (select pro_val cotz3, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =6 and zd.zone_key =3) t18
		on t1.obs_time = t18.obs_time

		join (select pro_val dosage, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =28) t19
		on t1.obs_time = t19.obs_time
		
		join (select pro_val fuelflwz1, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =9 and zd.zone_key =1) t20
		on t1.obs_time = t20.obs_time
		
		join (select pro_val fuelflwz2, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =9 and zd.zone_key =2) t21
		on t1.obs_time = t21.obs_time
		
		join (select pro_val fuelflwz3, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =9 and zd.zone_key =3) t22
		on t1.obs_time = t22.obs_time
		
		join (select pro_val fuelwallz1, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =10 and zd.zone_key =1) t23
		on t1.obs_time = t23.obs_time
		
		join (select pro_val fuelwallz2, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =10 and zd.zone_key =2) t24
		on t1.obs_time = t24.obs_time
		
		join (select pro_val fuelwallz3, obs_time
	from public.process_tags pt
		join tag_map tm on tm.map_key = pt.map_key
		join zone_dim zd on zd.zone_key =tm.zone_key
	where tm.param_key =10 and zd.zone_key =3) t25
		on t1.obs_time = t25.obs_time;"""

# CPR_SOR_EOR = '''SELECT min(t7.cprz1) as SORCPR_z1, max(t7.cprz1) as EORCPR_Z1,
#  min(t8.cprz2) as SORCPR_Z2, max(t8.cprz2) as EORCPR_Z2,
#   min(t9.cprz3) as SORCPR_Z3, max(t9.cprz3) as EORCPR_Z3
#
# from
# 	(select obs_time, run, run_hours, pro_val cprz1
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 		join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
# 	where tm.param_key =1 and zd.zone_key =1) t1
# 	join (select pro_val cprz1,  pt.obs_time
# from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =7) t7
# 		 on t1.obs_time = t7.obs_time
#
# 		 join (select pro_val cprz2, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =7 and zd.zone_key =2) t8
# 		on t1.obs_time = t8.obs_time
# 		join (select pro_val cprz3, obs_time
# 	from public.process_tags pt
# 		join tag_map tm on tm.map_key = pt.map_key
# 		join zone_dim zd on zd.zone_key =tm.zone_key
# 	where tm.param_key =7 and zd.zone_key =3) t9
# 		on t1.obs_time = t9.obs_time'''

CPR_SOR_EOR = '''SELECT json_build_object('TMT',(SELECT json_agg(json_build_object('obs_time' ,obs_time,'Zone1',tmtz1,
'Zone2',tmtz2,'Zone3',tmtz3,'uom','°C' ))from raw_data where run='{run}' and obs_time=(select {min_max}(obs_time) from raw_data 
where run='{run}')), 'CPR',(SELECT json_agg(json_build_object('obs_time' ,obs_time,'Zone1',cprz1,'Zone2',cprz2,'Zone3',
cprz2,'uom','Ratio' ))from raw_data where run='{run}' and obs_time=(select {min_max}(obs_time) from raw_data where run='{run}')))
'''

OVR_VIEW = '''SELECT json_build_object('data', (SELECT json_agg(json_build_object('obs_time'
,obs_time,'tmtz1',tmtz1,'tmtz2',tmtz2,'tmtz3',tmtz3,'cprz1',cprz1,'cprz2',cprz2,'cprz3',cprz2
, 'efrz1', efrz1, 'efrz2', efrz2, 'efrz3', efrz3, 'shcrz1', shcrz1,'shcrz2', shcrz2, 'shcrz3', shcrz3,
'cotz1', cotz1, 'cotz2', cotz2, 'cotz3', cotz3, 'fgffz1', fgffz1, 'fgffz2', fgffz2, 'fgffz3', fgffz3
))from raw_data where run={run}))'''

FRL_MULTI_LINE_GRAPH = """SELECT json_build_object('Ethane Feed', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp',extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val,'uom',pd.uom))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name ='Ethane Feed' and zd.zone_name='{Zone}' and run={run}),
'Dilution Steam', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp',extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val, 'uom',pd.uom))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name ='Dilution Steam' and zd.zone_name='{Zone}' and run={run}),
'CPR', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp',extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val,'uom', pd.uom ))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name ='CPR' and zd.zone_name='{Zone}' and run={run}),
'TMT', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp',extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val, 'uom', pd.uom))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name ='TMT' and zd.zone_name='{Zone}' and run={run}),
'COT', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp',extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val, 'uom' ,pd.uom))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name ='COT' and zd.zone_name='{Zone}' and run={run}),   
'SHC', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp',extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val, 'uom' ,pd.uom))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name ='SHC Ratio'and zd.zone_name='{Zone}' and run={run}),
'Dosage', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp',extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val, 'uom', pd.uom))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name ='DOSAGE' and run={run}),
'Fuel Gas Flow  (Floor)', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp',extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val, 'uom', pd.uom))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name ='Fuel Gas Flow  (Floor)' and zd.zone_name='{Zone}' and run={run}),
'Fuel Flow (Wall)', (SELECT json_agg(json_build_object('param_name',pm.param_name,'obs_time',obs_time,'timestamp',extract(epoch from obs_time),'run',run,'run_hours',run_hours,'pro_val',pro_val, 'uom', pd.uom))
from process_tags pt
join tag_map tm on tm.map_key = pt.map_key
join zone_dim zd on zd.zone_key =tm.zone_key
join param_cat_dim pcd on tm.param_cat_key = pcd.param_cat_key
join parameter_dim pm on tm.param_key=pm.param_key
join parameter_dim pd on pd.param_key=tm.param_key
where pm.param_name ='Fuel Flow (Wall)' and zd.zone_name='{Zone}' and run={run})
)"""

FRL_OVR_DATA = """
SELECT json_build_object('CPR', (SELECT json_agg(json_build_object('obs_time' ,obs_time, 
'Zone1', cprz1, 'Zone2', cprz2, 'Zone3', cprz3,'uom','Kg/hr','runlength',runlength ))from raw_data where run='{run}' and obs_time=(select max(
obs_time) from raw_data where run='{run}')), 'TMT',(SELECT json_agg(json_build_object('obs_time' ,obs_time,'Zone1',tmtz1,
'Zone2',tmtz2,'Zone3',tmtz3,'uom','°C' ))from raw_data where run='{run}' and obs_time=(select max(obs_time) from raw_data 
where run='{run}')), 'COT',(SELECT json_agg(json_build_object('obs_time' ,obs_time, 'Zone1', cotz1, 'Zone2', cotz2, 'Zone3', cotz3,'uom',
'%' ))from raw_data where run='{run}' and obs_time=(select max(obs_time) from raw_data where run='{run}')), 
'Ethane Feed',(SELECT json_agg(json_build_object('obs_time' ,obs_time, 
'Zone1', efrz1, 'Zone2', efrz2, 'Zone3', efrz3,'uom','Kg/hr','runlength',runlength))from raw_data where run='{run}' and obs_time=(select max(obs_time) from raw_data where run='{run}')), 'COT',
(SELECT json_agg(json_build_object('obs_time' ,obs_time, 'Zone1', cotz1, 'Zone2', cotz2, 'Zone3', cotz3,'uom',
'%'))from raw_data where run='{run}' and obs_time=(select max(obs_time) from raw_data where run='{run}')), 
'SHC Ratio',(SELECT json_agg(json_build_object('obs_time' ,obs_time, 'Zone1', shcrz1,'Zone2', shcrz2, 'Zone3', shcrz3,
'uom','%'))from raw_data where run='{run}' and obs_time=(select max(obs_time) from raw_data where run='{run}')))"""

MAX_RUN = """select max(run) from raw_data where obs_time=(select max(obs_time) from raw_data)"""

RUN_LIST = """select distinct run from raw_data order by run"""

MEAN_SUM_DATA = """select res.* from (select 'CPR' as paramname, avg(rd.cprz1) as Zone1, avg(rd.cprz2) as Zone2, avg(rd.cprz3) as Zone3,'Ratio' as uom,1 as ord from public.raw_data rd where rd.run='{run}'
union 
select 'TMT' as paramname, avg(rd.tmtz1) as Zone1, avg(rd.tmtz2) as Zone2, avg(rd.tmtz3) as Zone3,'°C' as uom,2 as ord from public.raw_data rd where rd.run='{run}'
union
select 'COT' as paramname, avg(rd.cotz1) as Zone1, avg(rd.cotz2) as Zone2, avg(rd.cotz3) as Zone3,'°C' as uom,3 as ord from public.raw_data rd where rd.run='{run}'
union
select 'Ethane Feed' as paramname, sum(rd.efrz1) as Zone1, sum(rd.efrz2) as Zone2, sum(rd.efrz3) as Zone3,'Tones' as uom,4 as ord from public.raw_data rd where rd.run='{run}'
union
select 'SHC Ratio' as paramname, avg(rd.shcrz1) as Zone1, avg(rd.shcrz2) as Zone2, avg(rd.shcrz3) as Zone3,'%' as uom,5 as ord from public.raw_data rd where rd.run='{run}')res order by ord
"""

OPTIMIZED_DATA_SUM_MEAN = """select 'SHC Ratio' as paramname, avg(rd.shcrz1) as Zone1, avg(rd.shcrz2) as Zone2, avg(rd.shcrz3) as Zone3,'%' as uom from public.optimised_data rd where rd.run='{run}'
union
select 'Ethane Feed' as paramname, sum(rd.efrz1) as Zone1, sum(rd.efrz2) as Zone2, sum(rd.efrz3) as Zone3,'Tones' as uom from public.optimised_data rd where rd.run='{run}'
union 
select 'COT' as paramname, avg(rd.cot1) as Zone1, avg(rd.cot2) as Zone2, avg(rd.cot3) as Zone3,'°C' as uom from public.optimised_data rd where rd.run='{run}'
"""

RUN_OPTIMISED_DATA = """SELECT json_build_object('Ethane Feed', (SELECT json_agg(json_build_object('obs_time' ,obs_time, 
'Zone1', efrz1, 'Zone2', efrz2, 'Zone3', efrz3,'uom','Kg/hr'))from  public.optimised_data where run='{run}'),
'SHC Ratio',(SELECT json_agg(json_build_object('obs_time' ,obs_time, 'Zone1', shcrz1,'Zone2', shcrz2, 'Zone3', shcrz3,
'uom','%'))from  public.optimised_data where run='{run}'), 'COT',
(SELECT json_agg(json_build_object('obs_time' ,obs_time, 'Zone1', cot1, 'Zone2', cot2, 'Zone3', cot3,'uom',
'%'))from  public.optimised_data where run='{run} and obs_time'))"""

OPTIMISED_MAX_RUN = """select max(run) from  public.optimised_data"""

UPLOAD_DETAILS = """INSERT INTO public.users(
	first_name, last_name, login_id, email_id, password, id)
	VALUES ('{first_name}', '{last_name}', '{login_id}', '{email_id}', '{password}', '{id}');"""

UPLOAD_RAW_DATA = """INSERT INTO public.raw_data( obs_time, run, runlength, efrz1, efrz2, efrz3, dsfz1, dsfz2, dsf3, 
shcrz1, shcrz2, shcrz3, cotp3, cotp1, cotp6, cotp5, cptp2, cotp4, cotz1, cotz2, cotz3, cprz1, cprz2, cprz3, tmtz1, 
tmtz2, tmtz3, ptle_temp, stle_temp, fgffz1, ffwz1, fgffz2, ffwz2, fgffz3, ffwz3, fgpfz1, fgpwz1, fgpfz2, fgpwz2, 
fgpfz3, fgpwz3, bwt, ofg, fd, shst, shsp, dosage, es, cpr_z1_c1, cpr_z1_c2, cpr_z1_c3, cpr_z1_c4, cpr_z1_c5, 
cpr_z1_c6, cpr_z1_c7, cpr_z1_c8, cpr_z2_c1, cprz2_c2, cprz2_c3, cprz2_c4, cprz2_c5, cprz2_c6, cprz2_c7, cprz2_c8, 
cprz3_c1, cprz3_c2, cprz3_c3, cprz3_c4, cprz3_c5, cprz3_c6, cprz3_c7, cprz3_c8, max_cpr) VALUES ('{obs_time}', {run}, 
{runlength},{efrz1},{efrz2},{efrz3}, {dsfz1}, {dsfz2}, {dsf3}, {shcrz1}, {shcrz2}, {shcrz3}, {cotp3}, {cotp1}, 
{cotp6}, {cotp5}, {cptp2}, {cotp4}, {cotz1}, {cotz2}, {cotz3}, {cprz1}, {cprz2}, {cprz3}, {tmtz1}, {tmtz2}, {tmtz3}, 
{ptle_temp}, {stle_temp}, {fgffz1}, {ffwz1}, {fgffz2}, {ffwz2}, {fgffz3}, {ffwz3}, {fgpfz1}, {fgpwz1}, {fgpfz2}, 
{fgpwz2}, {fgpfz3}, {fgpwz3}, {bwt}, {ofg}, {fd}, {shst},{shsp}, {dosage}, {es}, {cpr_z1_c1}, {cpr_z1_c2}, 
{cpr_z1_c3}, {cpr_z1_c4}, {cpr_z1_c5}, {cpr_z1_c6}, {cpr_z1_c7}, {cpr_z1_c8}, {cpr_z2_c1}, {cprz2_c2}, {cprz2_c3}, 
{cprz2_c4}, {cprz2_c5}, {cprz2_c6}, {cprz2_c7}, {cprz2_c8}, {cprz3_c1}, {cprz3_c2}, {cprz3_c3}, {cprz3_c4}, 
{cprz3_c5}, {cprz3_c6}, {cprz3_c7}, {cprz3_c8}, {max_cpr}); """

OPTIMISED_GRAPH__DATA = """SELECT json_build_object('optimised_data', (SELECT json_agg(json_build_object('param_name','{param_name}','obs_time',obs_time,'timestamp', extract(epoch from obs_time),'run',run,'pro_val',{column}, 'uom','{uom}'))
from optimised_data
where run='{run}'))"""

OPTIMISED_MULTI_LINE_GRAPH = """SELECT json_build_object('Ethane Feed',(SELECT json_agg(json_build_object(
'param_name','Ethane Feed','obs_time',obs_time,'timestamp', extract(epoch from obs_time),'run',run,'pro_val',
{Ethane}, 'uom','Kg/hr')) from optimised_data where run='{run}'), 'SHC Ratio',(SELECT json_agg(json_build_object(
'param_name','SHC Ratio','obs_time',obs_time,'timestamp', extract(epoch from obs_time),'run',run,'pro_val',{SHC}, 
'uom','%')) from optimised_data where run='{run}'), 'COT',(SELECT json_agg(json_build_object('param_name','COT',
'obs_time',obs_time,'timestamp', extract(epoch from obs_time),'run',run,'pro_val',{cot}, 'uom','°C')) from 
optimised_data where run='{run}')) """

OPTIMISED_RUN_LENGTH = """select count(max_cpr)/3 as run_length from optimised_data where run='{run}'"""

OPTIMISED_DATA = """select res.* from (select obs_time,'COT' as parameter,cot1 as Zone1,cot2 as Zone2,cot3 as Zone3,'%' as uom,1 as ord from optimised_data where run='{run}' and obs_time=(select max(obs_time) from optimised_data where run='{run}')
union 
select obs_time,'Ethane Feed' as parameter,efrz1 as Zone1,efrz2 as Zone2,efrz3 as Zone3,'Kg/hr' as uom ,2 as ord from optimised_data where run='{run}' and obs_time=(select max(obs_time) from optimised_data where run='{run}')
union
select obs_time,'SHC Ratio' as parameter,shcrz1 as Zone1,shcrz2 as Zone2,shcrz3 as Zone3,'%' as uom,3 as ord from optimised_data where run='{run}' and obs_time=(select max(obs_time) from optimised_data where run='{run}'))res order by ord 

"""