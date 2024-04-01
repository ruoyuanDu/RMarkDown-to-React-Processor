import React from 'react';
import FilteringJoinTwoDatasets from '../RDataWrangling/dplyr/contents/17-filtering-join-two-datasets_output_react'
import RepeatedOperationsOnMultipleColumn from '../RDataWrangling/dplyr/contents/13-repeated-operations-on-multiple-column_output_react'
import CrossJoinTwoDatasets from '../RDataWrangling/dplyr/contents/19-cross-join-two-datasets_output_react'
import KeepDistinctRows from '../RDataWrangling/dplyr/contents/7-keep-distinct-rows_output_react'
import GroupedDataset from '../RDataWrangling/dplyr/contents/5-2-grouped-dataset_output_react'
import CountObservations from '../RDataWrangling/dplyr/contents/15-count-observations_output_react'
import ReorderColumns from '../RDataWrangling/dplyr/contents/12-reorder-columns_output_react'
import SetOperations from '../RDataWrangling/dplyr/contents/21-set-operations_output_react'
import BetweenARange from '../RDataWrangling/dplyr/contents/22-between-a-range_output_react'
import ExtractASingleColumn from '../RDataWrangling/dplyr/contents/10-extract-a-single-column_output_react'
import SelectRows from '../RDataWrangling/dplyr/contents/8-select-rows_output_react'
import MutatingJoinTwoDatasets from '../RDataWrangling/dplyr/contents/16-mutating-join-two-datasets_output_react'
import BindTwoDatasetsByColumnsRows from '../RDataWrangling/dplyr/contents/20-bind-two-datasets-by-columns-rows_output_react'
import CountUniqueValues from '../RDataWrangling/dplyr/contents/23-count-unique-values_output_react'
import GlimpseColumns from '../RDataWrangling/dplyr/contents/9-glimpse-columns_output_react'
import DataMasking from '../RDataWrangling/dplyr/contents/24-data-masking_output_react'
import SelectColumns from '../RDataWrangling/dplyr/contents/2-select-columns_output_react'
import Summarize from '../RDataWrangling/dplyr/contents/5-1-summarize_output_react'
import FilterRows from '../RDataWrangling/dplyr/contents/3-filter-rows_output_react'
import Introduction from '../RDataWrangling/dplyr/contents/0-introduction_output_react'
import NestJoinTwoDatasets from '../RDataWrangling/dplyr/contents/18-nest-join-two-datasets_output_react'
import MutateColumns from '../RDataWrangling/dplyr/contents/4-mutate-columns_output_react'
import Arrange from '../RDataWrangling/dplyr/contents/6-arrange_output_react'
import RenameColumns from '../RDataWrangling/dplyr/contents/11-rename-columns_output_react'
import PipeOperator from '../RDataWrangling/dplyr/contents/1-pipe-operator_output_react'
import RowwiseOperations from '../RDataWrangling/dplyr/contents/14-rowwise-operations_output_react'
const data=[{'component': '<FilteringJoinTwoDatasets />', 'path': '17-filtering-join-two-datasets', 'title': '17 filtering join two datasets'},
{'component': '<RepeatedOperationsOnMultipleColumn />', 'path': '13-repeated-operations-on-multiple-column', 'title': '13 repeated operations on multiple column'},
{'component': '<CrossJoinTwoDatasets />', 'path': '19-cross-join-two-datasets', 'title': '19 cross join two datasets'},
{'component': '<KeepDistinctRows />', 'path': '7-keep-distinct-rows', 'title': '7 keep distinct rows'},
{'component': '<GroupedDataset />', 'path': '5-2-grouped-dataset', 'title': '5 2 grouped dataset'},
{'component': '<CountObservations />', 'path': '15-count-observations', 'title': '15 count observations'},
{'component': '<ReorderColumns />', 'path': '12-reorder-columns', 'title': '12 reorder columns'},
{'component': '<SetOperations />', 'path': '21-set-operations', 'title': '21 set operations'},
{'component': '<BetweenARange />', 'path': '22-between-a-range', 'title': '22 between a range'},
{'component': '<ExtractASingleColumn />', 'path': '10-extract-a-single-column', 'title': '10 extract a single column'},
{'component': '<SelectRows />', 'path': '8-select-rows', 'title': '8 select rows'},
{'component': '<MutatingJoinTwoDatasets />', 'path': '16-mutating-join-two-datasets', 'title': '16 mutating join two datasets'},
{'component': '<BindTwoDatasetsByColumnsRows />', 'path': '20-bind-two-datasets-by-columns-rows', 'title': '20 bind two datasets by columns rows'},
{'component': '<CountUniqueValues />', 'path': '23-count-unique-values', 'title': '23 count unique values'},
{'component': '<GlimpseColumns />', 'path': '9-glimpse-columns', 'title': '9 glimpse columns'},
{'component': '<DataMasking />', 'path': '24-data-masking', 'title': '24 data masking'},
{'component': '<SelectColumns />', 'path': '2-select-columns', 'title': '2 select columns'},
{'component': '<Summarize />', 'path': '5-1-summarize', 'title': '5 1 summarize'},
{'component': '<FilterRows />', 'path': '3-filter-rows', 'title': '3 filter rows'},
{'component': '<Introduction />', 'path': '0-introduction', 'title': '0 introduction'},
{'component': '<NestJoinTwoDatasets />', 'path': '18-nest-join-two-datasets', 'title': '18 nest join two datasets'},
{'component': '<MutateColumns />', 'path': '4-mutate-columns', 'title': '4 mutate columns'},
{'component': '<Arrange />', 'path': '6-arrange', 'title': '6 arrange'},
{'component': '<RenameColumns />', 'path': '11-rename-columns', 'title': '11 rename columns'},
{'component': '<PipeOperator />', 'path': '1-pipe-operator', 'title': '1 pipe operator'},
{'component': '<RowwiseOperations />', 'path': '14-rowwise-operations', 'title': '14 rowwise operations'},
]