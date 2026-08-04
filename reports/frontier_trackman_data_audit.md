# Frontier League TrackMan Parquet Data Audit

- File: `data\raw\2026-data.parquet`
- Rows: 199,368
- Columns: 242
- Memory usage in pandas: 1,253.28 MB

## 1. All Column Names
1. `session_id`
2. `source_endpoint`
3. `source_file`
4. `play_id`
5. `track_id`
6. `play_match_key`
7. `ball_match_key`
8. `version`
9. `pitch_uid`
10. `local_date_time`
11. `utc_date_time`
12. `kor_bb`
13. `notes`
14. `tagger_behavior_pitch_no`
15. `tagger_behavior_p_aofinning`
16. `tagger_behavior_pitchof_pa`
17. `pitcher_name`
18. `pitcher_id`
19. `pitcher_throws`
20. `pitcher_team`
21. `batter_name`
22. `batter_id`
23. `batter_side`
24. `batter_team`
25. `catcher_name`
26. `catcher_id`
27. `catcher_throws`
28. `catcher_team`
29. `game_state_inning`
30. `game_state_top_bottom`
31. `game_state_outs`
32. `game_state_balls`
33. `game_state_strikes`
34. `pitch_tag_tagged_pitch_type`
35. `pitch_tag_pitch_call`
36. `pitch_tag_auto_pitch_type`
37. `hit_tag_tagged_hit_type`
38. `play_result_play_result`
39. `play_result_outs_on_play`
40. `play_result_runs_scored`
41. `hit_tag_auto_hit_type`
42. `strike_zone_top`
43. `strike_zone_bottom`
44. `strike_zone_right`
45. `strike_zone_left`
46. `strike_zone_type`
47. `strike_zone_decision`
48. `pitch_tracking_session_id`
49. `pitch_tracking_source_endpoint`
50. `pitch_tracking_source_file`
51. `pitch_tracking_play_id`
52. `pitch_tracking_track_id`
53. `pitch_tracking_ball_match_key`
54. `pitch_tracking_version`
55. `play_id_x`
56. `track_id_x`
57. `pitch_tracking_track_start_time`
58. `pitch_tracking_kind`
59. `pitch_release_rel_speed_x`
60. `pitch_release_spin_rate_x`
61. `pitch_release_extension_x`
62. `pitch_release_vert_rel_angle_x`
63. `pitch_release_horz_rel_angle_x`
64. `pitch_release_rel_height_x`
65. `pitch_release_rel_side_x`
66. `pitch_release_confidence_x`
67. `pitch_movement_horz_break_x`
68. `pitch_movement_vert_break_x`
69. `pitch_movement_induced_vert_break_x`
70. `pitch_movement_spin_axis_x`
71. `pitch_movement_tilt_x`
72. `pitch_movement_confidence_x`
73. `pitch_location_zone_time_x`
74. `pitch_location_plate_loc_height_x`
75. `pitch_location_plate_loc_side_x`
76. `pitch_location_zone_speed_x`
77. `pitch_location_vert_appr_angle_x`
78. `pitch_location_horz_appr_angle_x`
79. `pitch_location_confidence_x`
80. `pitch_nine_p_x0_x_x`
81. `pitch_nine_p_x0_y_x`
82. `pitch_nine_p_x0_z_x`
83. `pitch_nine_p_v0_x_x`
84. `pitch_nine_p_v0_y_x`
85. `pitch_nine_p_v0_z_x`
86. `pitch_nine_p_a0_x_x`
87. `pitch_nine_p_a0_y_x`
88. `pitch_nine_p_a0_z_x`
89. `pitch_nine_p_pfxx_x`
90. `pitch_nine_p_pfxz_x`
91. `pitch_speed_drop_x`
92. `pitch_flight_poly_fit_pitch_trajectory_x_x`
93. `pitch_flight_poly_fit_pitch_trajectory_y_x`
94. `pitch_flight_poly_fit_pitch_trajectory_z_x`
95. `pitch_effective_velo_x`
96. `catcher_throw_pop_time_x`
97. `catcher_throw_exchange_time_x`
98. `catcher_throw_catch_catch_position_x_x`
99. `catcher_throw_catch_catch_position_y_x`
100. `catcher_throw_catch_catch_position_z_x`
101. `catcher_throw_catch_confidence_x`
102. `catcher_throw_throw_throw_speed_x`
103. `catcher_throw_throw_throw_position_x_x`
104. `catcher_throw_throw_throw_position_y_x`
105. `catcher_throw_throw_throw_position_z_x`
106. `catcher_throw_location_time_to_base_x`
107. `catcher_throw_location_base_position_x_x`
108. `catcher_throw_location_base_position_y_x`
109. `catcher_throw_location_base_position_z_x`
110. `catcher_throw_location_confidence_x`
111. `catcher_throw_flight_poly_fit_throw_trajectory_x_x`
112. `catcher_throw_flight_poly_fit_throw_trajectory_y_x`
113. `catcher_throw_flight_poly_fit_throw_trajectory_z_x`
114. `hit_launch_exit_speed_x`
115. `hit_launch_contact_position_x_x`
116. `hit_launch_contact_position_y_x`
117. `hit_launch_contact_position_z_x`
118. `hit_launch_angle_x`
119. `hit_launch_direction_x`
120. `hit_launch_confidence_x`
121. `hit_landing_flat_distance_x`
122. `hit_landing_flat_bearing_x`
123. `hit_landing_flat_hang_time_x`
124. `hit_landing_flat_confidence_x`
125. `hit_last_tracked_distance_x`
126. `hit_max_height_x`
127. `hit_flight_poly_fit_hit_trajectory_x_x`
128. `hit_flight_poly_fit_hit_trajectory_y_x`
129. `hit_flight_poly_fit_hit_trajectory_z_x`
130. `hit_launch_hit_spin_axis_x`
131. `hit_launch_hit_spin_rate_x`
132. `hit_position_at110_feet_x_x`
133. `hit_position_at110_feet_y_x`
134. `hit_position_at110_feet_z_x`
135. `hit_tracking_session_id`
136. `hit_tracking_source_endpoint`
137. `hit_tracking_source_file`
138. `hit_tracking_play_id`
139. `hit_tracking_track_id`
140. `hit_tracking_ball_match_key`
141. `hit_tracking_version`
142. `play_id_y`
143. `track_id_y`
144. `hit_tracking_track_start_time`
145. `hit_tracking_kind`
146. `pitch_release_rel_speed_y`
147. `pitch_release_spin_rate_y`
148. `pitch_release_extension_y`
149. `pitch_release_vert_rel_angle_y`
150. `pitch_release_horz_rel_angle_y`
151. `pitch_release_rel_height_y`
152. `pitch_release_rel_side_y`
153. `pitch_release_confidence_y`
154. `pitch_movement_horz_break_y`
155. `pitch_movement_vert_break_y`
156. `pitch_movement_induced_vert_break_y`
157. `pitch_movement_spin_axis_y`
158. `pitch_movement_tilt_y`
159. `pitch_movement_confidence_y`
160. `pitch_location_zone_time_y`
161. `pitch_location_plate_loc_height_y`
162. `pitch_location_plate_loc_side_y`
163. `pitch_location_zone_speed_y`
164. `pitch_location_vert_appr_angle_y`
165. `pitch_location_horz_appr_angle_y`
166. `pitch_location_confidence_y`
167. `pitch_nine_p_x0_x_y`
168. `pitch_nine_p_x0_y_y`
169. `pitch_nine_p_x0_z_y`
170. `pitch_nine_p_v0_x_y`
171. `pitch_nine_p_v0_y_y`
172. `pitch_nine_p_v0_z_y`
173. `pitch_nine_p_a0_x_y`
174. `pitch_nine_p_a0_y_y`
175. `pitch_nine_p_a0_z_y`
176. `pitch_nine_p_pfxx_y`
177. `pitch_nine_p_pfxz_y`
178. `pitch_speed_drop_y`
179. `pitch_flight_poly_fit_pitch_trajectory_x_y`
180. `pitch_flight_poly_fit_pitch_trajectory_y_y`
181. `pitch_flight_poly_fit_pitch_trajectory_z_y`
182. `pitch_effective_velo_y`
183. `catcher_throw_pop_time_y`
184. `catcher_throw_exchange_time_y`
185. `catcher_throw_catch_catch_position_x_y`
186. `catcher_throw_catch_catch_position_y_y`
187. `catcher_throw_catch_catch_position_z_y`
188. `catcher_throw_catch_confidence_y`
189. `catcher_throw_throw_throw_speed_y`
190. `catcher_throw_throw_throw_position_x_y`
191. `catcher_throw_throw_throw_position_y_y`
192. `catcher_throw_throw_throw_position_z_y`
193. `catcher_throw_location_time_to_base_y`
194. `catcher_throw_location_base_position_x_y`
195. `catcher_throw_location_base_position_y_y`
196. `catcher_throw_location_base_position_z_y`
197. `catcher_throw_location_confidence_y`
198. `catcher_throw_flight_poly_fit_throw_trajectory_x_y`
199. `catcher_throw_flight_poly_fit_throw_trajectory_y_y`
200. `catcher_throw_flight_poly_fit_throw_trajectory_z_y`
201. `hit_launch_exit_speed_y`
202. `hit_launch_contact_position_x_y`
203. `hit_launch_contact_position_y_y`
204. `hit_launch_contact_position_z_y`
205. `hit_launch_angle_y`
206. `hit_launch_direction_y`
207. `hit_launch_confidence_y`
208. `hit_landing_flat_distance_y`
209. `hit_landing_flat_bearing_y`
210. `hit_landing_flat_hang_time_y`
211. `hit_landing_flat_confidence_y`
212. `hit_last_tracked_distance_y`
213. `hit_max_height_y`
214. `hit_flight_poly_fit_hit_trajectory_x_y`
215. `hit_flight_poly_fit_hit_trajectory_y_y`
216. `hit_flight_poly_fit_hit_trajectory_z_y`
217. `hit_launch_hit_spin_axis_y`
218. `hit_launch_hit_spin_rate_y`
219. `hit_position_at110_feet_x_y`
220. `hit_position_at110_feet_y_y`
221. `hit_position_at110_feet_z_y`
222. `has_pitch_tracking`
223. `has_hit_tracking`
224. `has_any_tracking`
225. `pitch_tag_tagged_pitch_type_canonical`
226. `pitch_tag_auto_pitch_type_canonical`
227. `pitch_tag_pitch_call_canonical`
228. `hit_tag_tagged_hit_type_canonical`
229. `hit_tag_auto_hit_type_canonical`
230. `play_result_play_result_canonical`
231. `pitcher_throws_canonical`
232. `batter_side_canonical`
233. `catcher_throws_canonical`
234. `pitch_type`
235. `pitch_type_source`
236. `hit_type`
237. `hit_type_source`
238. `play_result`
239. `pitch_call`
240. `has_core_context`
241. `pitch_tracking_kind_normalized`
242. `hit_tracking_kind_normalized`

## 2. Data Types
| Column | Data Type |
|---|---|
| `session_id` | `object` |
| `source_endpoint` | `object` |
| `source_file` | `object` |
| `play_id` | `object` |
| `track_id` | `object` |
| `play_match_key` | `object` |
| `ball_match_key` | `object` |
| `version` | `object` |
| `pitch_uid` | `object` |
| `local_date_time` | `datetime64[ns]` |
| `utc_date_time` | `datetime64[ns, UTC]` |
| `kor_bb` | `object` |
| `notes` | `object` |
| `tagger_behavior_pitch_no` | `Int64` |
| `tagger_behavior_p_aofinning` | `Int64` |
| `tagger_behavior_pitchof_pa` | `float64` |
| `pitcher_name` | `object` |
| `pitcher_id` | `object` |
| `pitcher_throws` | `object` |
| `pitcher_team` | `object` |
| `batter_name` | `object` |
| `batter_id` | `object` |
| `batter_side` | `object` |
| `batter_team` | `object` |
| `catcher_name` | `object` |
| `catcher_id` | `object` |
| `catcher_throws` | `object` |
| `catcher_team` | `object` |
| `game_state_inning` | `Int64` |
| `game_state_top_bottom` | `object` |
| `game_state_outs` | `Int64` |
| `game_state_balls` | `Int64` |
| `game_state_strikes` | `Int64` |
| `pitch_tag_tagged_pitch_type` | `object` |
| `pitch_tag_pitch_call` | `object` |
| `pitch_tag_auto_pitch_type` | `object` |
| `hit_tag_tagged_hit_type` | `object` |
| `play_result_play_result` | `object` |
| `play_result_outs_on_play` | `Int64` |
| `play_result_runs_scored` | `Int64` |
| `hit_tag_auto_hit_type` | `object` |
| `strike_zone_top` | `float64` |
| `strike_zone_bottom` | `float64` |
| `strike_zone_right` | `float64` |
| `strike_zone_left` | `float64` |
| `strike_zone_type` | `object` |
| `strike_zone_decision` | `object` |
| `pitch_tracking_session_id` | `object` |
| `pitch_tracking_source_endpoint` | `object` |
| `pitch_tracking_source_file` | `object` |
| `pitch_tracking_play_id` | `object` |
| `pitch_tracking_track_id` | `object` |
| `pitch_tracking_ball_match_key` | `object` |
| `pitch_tracking_version` | `object` |
| `play_id_x` | `object` |
| `track_id_x` | `object` |
| `pitch_tracking_track_start_time` | `object` |
| `pitch_tracking_kind` | `object` |
| `pitch_release_rel_speed_x` | `float64` |
| `pitch_release_spin_rate_x` | `float64` |
| `pitch_release_extension_x` | `float64` |
| `pitch_release_vert_rel_angle_x` | `float64` |
| `pitch_release_horz_rel_angle_x` | `float64` |
| `pitch_release_rel_height_x` | `float64` |
| `pitch_release_rel_side_x` | `float64` |
| `pitch_release_confidence_x` | `object` |
| `pitch_movement_horz_break_x` | `float64` |
| `pitch_movement_vert_break_x` | `float64` |
| `pitch_movement_induced_vert_break_x` | `float64` |
| `pitch_movement_spin_axis_x` | `float64` |
| `pitch_movement_tilt_x` | `object` |
| `pitch_movement_confidence_x` | `object` |
| `pitch_location_zone_time_x` | `float64` |
| `pitch_location_plate_loc_height_x` | `float64` |
| `pitch_location_plate_loc_side_x` | `float64` |
| `pitch_location_zone_speed_x` | `float64` |
| `pitch_location_vert_appr_angle_x` | `float64` |
| `pitch_location_horz_appr_angle_x` | `float64` |
| `pitch_location_confidence_x` | `object` |
| `pitch_nine_p_x0_x_x` | `float64` |
| `pitch_nine_p_x0_y_x` | `float64` |
| `pitch_nine_p_x0_z_x` | `float64` |
| `pitch_nine_p_v0_x_x` | `float64` |
| `pitch_nine_p_v0_y_x` | `float64` |
| `pitch_nine_p_v0_z_x` | `float64` |
| `pitch_nine_p_a0_x_x` | `float64` |
| `pitch_nine_p_a0_y_x` | `float64` |
| `pitch_nine_p_a0_z_x` | `float64` |
| `pitch_nine_p_pfxx_x` | `float64` |
| `pitch_nine_p_pfxz_x` | `float64` |
| `pitch_speed_drop_x` | `float64` |
| `pitch_flight_poly_fit_pitch_trajectory_x_x` | `object` |
| `pitch_flight_poly_fit_pitch_trajectory_y_x` | `object` |
| `pitch_flight_poly_fit_pitch_trajectory_z_x` | `object` |
| `pitch_effective_velo_x` | `float64` |
| `catcher_throw_pop_time_x` | `float64` |
| `catcher_throw_exchange_time_x` | `float64` |
| `catcher_throw_catch_catch_position_x_x` | `float64` |
| `catcher_throw_catch_catch_position_y_x` | `float64` |
| `catcher_throw_catch_catch_position_z_x` | `float64` |
| `catcher_throw_catch_confidence_x` | `object` |
| `catcher_throw_throw_throw_speed_x` | `float64` |
| `catcher_throw_throw_throw_position_x_x` | `float64` |
| `catcher_throw_throw_throw_position_y_x` | `float64` |
| `catcher_throw_throw_throw_position_z_x` | `float64` |
| `catcher_throw_location_time_to_base_x` | `float64` |
| `catcher_throw_location_base_position_x_x` | `float64` |
| `catcher_throw_location_base_position_y_x` | `float64` |
| `catcher_throw_location_base_position_z_x` | `float64` |
| `catcher_throw_location_confidence_x` | `object` |
| `catcher_throw_flight_poly_fit_throw_trajectory_x_x` | `object` |
| `catcher_throw_flight_poly_fit_throw_trajectory_y_x` | `object` |
| `catcher_throw_flight_poly_fit_throw_trajectory_z_x` | `object` |
| `hit_launch_exit_speed_x` | `float64` |
| `hit_launch_contact_position_x_x` | `float64` |
| `hit_launch_contact_position_y_x` | `float64` |
| `hit_launch_contact_position_z_x` | `float64` |
| `hit_launch_angle_x` | `float64` |
| `hit_launch_direction_x` | `float64` |
| `hit_launch_confidence_x` | `object` |
| `hit_landing_flat_distance_x` | `float64` |
| `hit_landing_flat_bearing_x` | `float64` |
| `hit_landing_flat_hang_time_x` | `float64` |
| `hit_landing_flat_confidence_x` | `object` |
| `hit_last_tracked_distance_x` | `float64` |
| `hit_max_height_x` | `float64` |
| `hit_flight_poly_fit_hit_trajectory_x_x` | `object` |
| `hit_flight_poly_fit_hit_trajectory_y_x` | `object` |
| `hit_flight_poly_fit_hit_trajectory_z_x` | `object` |
| `hit_launch_hit_spin_axis_x` | `float64` |
| `hit_launch_hit_spin_rate_x` | `float64` |
| `hit_position_at110_feet_x_x` | `float64` |
| `hit_position_at110_feet_y_x` | `float64` |
| `hit_position_at110_feet_z_x` | `float64` |
| `hit_tracking_session_id` | `object` |
| `hit_tracking_source_endpoint` | `object` |
| `hit_tracking_source_file` | `object` |
| `hit_tracking_play_id` | `object` |
| `hit_tracking_track_id` | `object` |
| `hit_tracking_ball_match_key` | `object` |
| `hit_tracking_version` | `object` |
| `play_id_y` | `object` |
| `track_id_y` | `object` |
| `hit_tracking_track_start_time` | `object` |
| `hit_tracking_kind` | `object` |
| `pitch_release_rel_speed_y` | `float64` |
| `pitch_release_spin_rate_y` | `float64` |
| `pitch_release_extension_y` | `float64` |
| `pitch_release_vert_rel_angle_y` | `float64` |
| `pitch_release_horz_rel_angle_y` | `float64` |
| `pitch_release_rel_height_y` | `float64` |
| `pitch_release_rel_side_y` | `float64` |
| `pitch_release_confidence_y` | `object` |
| `pitch_movement_horz_break_y` | `float64` |
| `pitch_movement_vert_break_y` | `float64` |
| `pitch_movement_induced_vert_break_y` | `float64` |
| `pitch_movement_spin_axis_y` | `float64` |
| `pitch_movement_tilt_y` | `object` |
| `pitch_movement_confidence_y` | `object` |
| `pitch_location_zone_time_y` | `float64` |
| `pitch_location_plate_loc_height_y` | `float64` |
| `pitch_location_plate_loc_side_y` | `float64` |
| `pitch_location_zone_speed_y` | `float64` |
| `pitch_location_vert_appr_angle_y` | `float64` |
| `pitch_location_horz_appr_angle_y` | `float64` |
| `pitch_location_confidence_y` | `object` |
| `pitch_nine_p_x0_x_y` | `float64` |
| `pitch_nine_p_x0_y_y` | `float64` |
| `pitch_nine_p_x0_z_y` | `float64` |
| `pitch_nine_p_v0_x_y` | `float64` |
| `pitch_nine_p_v0_y_y` | `float64` |
| `pitch_nine_p_v0_z_y` | `float64` |
| `pitch_nine_p_a0_x_y` | `float64` |
| `pitch_nine_p_a0_y_y` | `float64` |
| `pitch_nine_p_a0_z_y` | `float64` |
| `pitch_nine_p_pfxx_y` | `float64` |
| `pitch_nine_p_pfxz_y` | `float64` |
| `pitch_speed_drop_y` | `float64` |
| `pitch_flight_poly_fit_pitch_trajectory_x_y` | `object` |
| `pitch_flight_poly_fit_pitch_trajectory_y_y` | `object` |
| `pitch_flight_poly_fit_pitch_trajectory_z_y` | `object` |
| `pitch_effective_velo_y` | `float64` |
| `catcher_throw_pop_time_y` | `float64` |
| `catcher_throw_exchange_time_y` | `float64` |
| `catcher_throw_catch_catch_position_x_y` | `float64` |
| `catcher_throw_catch_catch_position_y_y` | `float64` |
| `catcher_throw_catch_catch_position_z_y` | `float64` |
| `catcher_throw_catch_confidence_y` | `object` |
| `catcher_throw_throw_throw_speed_y` | `float64` |
| `catcher_throw_throw_throw_position_x_y` | `float64` |
| `catcher_throw_throw_throw_position_y_y` | `float64` |
| `catcher_throw_throw_throw_position_z_y` | `float64` |
| `catcher_throw_location_time_to_base_y` | `float64` |
| `catcher_throw_location_base_position_x_y` | `float64` |
| `catcher_throw_location_base_position_y_y` | `float64` |
| `catcher_throw_location_base_position_z_y` | `float64` |
| `catcher_throw_location_confidence_y` | `object` |
| `catcher_throw_flight_poly_fit_throw_trajectory_x_y` | `object` |
| `catcher_throw_flight_poly_fit_throw_trajectory_y_y` | `object` |
| `catcher_throw_flight_poly_fit_throw_trajectory_z_y` | `object` |
| `hit_launch_exit_speed_y` | `float64` |
| `hit_launch_contact_position_x_y` | `float64` |
| `hit_launch_contact_position_y_y` | `float64` |
| `hit_launch_contact_position_z_y` | `float64` |
| `hit_launch_angle_y` | `float64` |
| `hit_launch_direction_y` | `float64` |
| `hit_launch_confidence_y` | `object` |
| `hit_landing_flat_distance_y` | `float64` |
| `hit_landing_flat_bearing_y` | `float64` |
| `hit_landing_flat_hang_time_y` | `float64` |
| `hit_landing_flat_confidence_y` | `object` |
| `hit_last_tracked_distance_y` | `float64` |
| `hit_max_height_y` | `float64` |
| `hit_flight_poly_fit_hit_trajectory_x_y` | `object` |
| `hit_flight_poly_fit_hit_trajectory_y_y` | `object` |
| `hit_flight_poly_fit_hit_trajectory_z_y` | `object` |
| `hit_launch_hit_spin_axis_y` | `float64` |
| `hit_launch_hit_spin_rate_y` | `float64` |
| `hit_position_at110_feet_x_y` | `float64` |
| `hit_position_at110_feet_y_y` | `float64` |
| `hit_position_at110_feet_z_y` | `float64` |
| `has_pitch_tracking` | `bool` |
| `has_hit_tracking` | `bool` |
| `has_any_tracking` | `bool` |
| `pitch_tag_tagged_pitch_type_canonical` | `string` |
| `pitch_tag_auto_pitch_type_canonical` | `string` |
| `pitch_tag_pitch_call_canonical` | `string` |
| `hit_tag_tagged_hit_type_canonical` | `string` |
| `hit_tag_auto_hit_type_canonical` | `string` |
| `play_result_play_result_canonical` | `string` |
| `pitcher_throws_canonical` | `string` |
| `batter_side_canonical` | `string` |
| `catcher_throws_canonical` | `string` |
| `pitch_type` | `string` |
| `pitch_type_source` | `string` |
| `hit_type` | `string` |
| `hit_type_source` | `string` |
| `play_result` | `string` |
| `pitch_call` | `string` |
| `has_core_context` | `bool` |
| `pitch_tracking_kind_normalized` | `string` |
| `hit_tracking_kind_normalized` | `string` |

## 3. Missing Values
| Column | Missing Count | Missing % |
|---|---:|---:|
| `session_id` | 0 | 0.00% |
| `source_endpoint` | 0 | 0.00% |
| `source_file` | 0 | 0.00% |
| `play_id` | 0 | 0.00% |
| `track_id` | 199,368 | 100.00% |
| `play_match_key` | 0 | 0.00% |
| `ball_match_key` | 199,368 | 100.00% |
| `version` | 0 | 0.00% |
| `pitch_uid` | 0 | 0.00% |
| `local_date_time` | 254 | 0.13% |
| `utc_date_time` | 251 | 0.13% |
| `kor_bb` | 0 | 0.00% |
| `notes` | 198,678 | 99.65% |
| `tagger_behavior_pitch_no` | 0 | 0.00% |
| `tagger_behavior_p_aofinning` | 1,347 | 0.68% |
| `tagger_behavior_pitchof_pa` | 1,347 | 0.68% |
| `pitcher_name` | 25 | 0.01% |
| `pitcher_id` | 1,532 | 0.77% |
| `pitcher_throws` | 0 | 0.00% |
| `pitcher_team` | 0 | 0.00% |
| `batter_name` | 4 | 0.00% |
| `batter_id` | 730 | 0.37% |
| `batter_side` | 7 | 0.00% |
| `batter_team` | 0 | 0.00% |
| `catcher_name` | 647 | 0.32% |
| `catcher_id` | 1,543 | 0.77% |
| `catcher_throws` | 0 | 0.00% |
| `catcher_team` | 0 | 0.00% |
| `game_state_inning` | 0 | 0.00% |
| `game_state_top_bottom` | 0 | 0.00% |
| `game_state_outs` | 0 | 0.00% |
| `game_state_balls` | 0 | 0.00% |
| `game_state_strikes` | 0 | 0.00% |
| `pitch_tag_tagged_pitch_type` | 0 | 0.00% |
| `pitch_tag_pitch_call` | 0 | 0.00% |
| `pitch_tag_auto_pitch_type` | 1,677 | 0.84% |
| `hit_tag_tagged_hit_type` | 0 | 0.00% |
| `play_result_play_result` | 0 | 0.00% |
| `play_result_outs_on_play` | 0 | 0.00% |
| `play_result_runs_scored` | 0 | 0.00% |
| `hit_tag_auto_hit_type` | 151,848 | 76.16% |
| `strike_zone_top` | 63,926 | 32.06% |
| `strike_zone_bottom` | 63,926 | 32.06% |
| `strike_zone_right` | 63,926 | 32.06% |
| `strike_zone_left` | 63,926 | 32.06% |
| `strike_zone_type` | 63,926 | 32.06% |
| `strike_zone_decision` | 63,926 | 32.06% |
| `pitch_tracking_session_id` | 1,651 | 0.83% |
| `pitch_tracking_source_endpoint` | 1,651 | 0.83% |
| `pitch_tracking_source_file` | 1,651 | 0.83% |
| `pitch_tracking_play_id` | 1,651 | 0.83% |
| `pitch_tracking_track_id` | 1,651 | 0.83% |
| `pitch_tracking_ball_match_key` | 1,651 | 0.83% |
| `pitch_tracking_version` | 1,651 | 0.83% |
| `play_id_x` | 1,651 | 0.83% |
| `track_id_x` | 1,651 | 0.83% |
| `pitch_tracking_track_start_time` | 1,651 | 0.83% |
| `pitch_tracking_kind` | 1,651 | 0.83% |
| `pitch_release_rel_speed_x` | 1,651 | 0.83% |
| `pitch_release_spin_rate_x` | 1,651 | 0.83% |
| `pitch_release_extension_x` | 1,671 | 0.84% |
| `pitch_release_vert_rel_angle_x` | 1,651 | 0.83% |
| `pitch_release_horz_rel_angle_x` | 1,651 | 0.83% |
| `pitch_release_rel_height_x` | 1,651 | 0.83% |
| `pitch_release_rel_side_x` | 1,651 | 0.83% |
| `pitch_release_confidence_x` | 1,651 | 0.83% |
| `pitch_movement_horz_break_x` | 1,672 | 0.84% |
| `pitch_movement_vert_break_x` | 1,672 | 0.84% |
| `pitch_movement_induced_vert_break_x` | 1,672 | 0.84% |
| `pitch_movement_spin_axis_x` | 1,672 | 0.84% |
| `pitch_movement_tilt_x` | 1,672 | 0.84% |
| `pitch_movement_confidence_x` | 1,672 | 0.84% |
| `pitch_location_zone_time_x` | 1,651 | 0.83% |
| `pitch_location_plate_loc_height_x` | 1,651 | 0.83% |
| `pitch_location_plate_loc_side_x` | 1,651 | 0.83% |
| `pitch_location_zone_speed_x` | 1,651 | 0.83% |
| `pitch_location_vert_appr_angle_x` | 1,651 | 0.83% |
| `pitch_location_horz_appr_angle_x` | 1,651 | 0.83% |
| `pitch_location_confidence_x` | 1,651 | 0.83% |
| `pitch_nine_p_x0_x_x` | 1,651 | 0.83% |
| `pitch_nine_p_x0_y_x` | 1,651 | 0.83% |
| `pitch_nine_p_x0_z_x` | 1,651 | 0.83% |
| `pitch_nine_p_v0_x_x` | 1,651 | 0.83% |
| `pitch_nine_p_v0_y_x` | 1,651 | 0.83% |
| `pitch_nine_p_v0_z_x` | 1,651 | 0.83% |
| `pitch_nine_p_a0_x_x` | 1,651 | 0.83% |
| `pitch_nine_p_a0_y_x` | 1,651 | 0.83% |
| `pitch_nine_p_a0_z_x` | 1,651 | 0.83% |
| `pitch_nine_p_pfxx_x` | 1,651 | 0.83% |
| `pitch_nine_p_pfxz_x` | 1,651 | 0.83% |
| `pitch_speed_drop_x` | 1,651 | 0.83% |
| `pitch_flight_poly_fit_pitch_trajectory_x_x` | 1,651 | 0.83% |
| `pitch_flight_poly_fit_pitch_trajectory_y_x` | 1,651 | 0.83% |
| `pitch_flight_poly_fit_pitch_trajectory_z_x` | 1,651 | 0.83% |
| `pitch_effective_velo_x` | 1,651 | 0.83% |
| `catcher_throw_pop_time_x` | 199,368 | 100.00% |
| `catcher_throw_exchange_time_x` | 199,368 | 100.00% |
| `catcher_throw_catch_catch_position_x_x` | 199,368 | 100.00% |
| `catcher_throw_catch_catch_position_y_x` | 199,368 | 100.00% |
| `catcher_throw_catch_catch_position_z_x` | 199,368 | 100.00% |
| `catcher_throw_catch_confidence_x` | 199,368 | 100.00% |
| `catcher_throw_throw_throw_speed_x` | 199,368 | 100.00% |
| `catcher_throw_throw_throw_position_x_x` | 199,368 | 100.00% |
| `catcher_throw_throw_throw_position_y_x` | 199,368 | 100.00% |
| `catcher_throw_throw_throw_position_z_x` | 199,368 | 100.00% |
| `catcher_throw_location_time_to_base_x` | 199,368 | 100.00% |
| `catcher_throw_location_base_position_x_x` | 199,368 | 100.00% |
| `catcher_throw_location_base_position_y_x` | 199,368 | 100.00% |
| `catcher_throw_location_base_position_z_x` | 199,368 | 100.00% |
| `catcher_throw_location_confidence_x` | 199,368 | 100.00% |
| `catcher_throw_flight_poly_fit_throw_trajectory_x_x` | 199,368 | 100.00% |
| `catcher_throw_flight_poly_fit_throw_trajectory_y_x` | 199,368 | 100.00% |
| `catcher_throw_flight_poly_fit_throw_trajectory_z_x` | 199,368 | 100.00% |
| `hit_launch_exit_speed_x` | 199,368 | 100.00% |
| `hit_launch_contact_position_x_x` | 199,368 | 100.00% |
| `hit_launch_contact_position_y_x` | 199,368 | 100.00% |
| `hit_launch_contact_position_z_x` | 199,368 | 100.00% |
| `hit_launch_angle_x` | 199,368 | 100.00% |
| `hit_launch_direction_x` | 199,368 | 100.00% |
| `hit_launch_confidence_x` | 199,368 | 100.00% |
| `hit_landing_flat_distance_x` | 199,368 | 100.00% |
| `hit_landing_flat_bearing_x` | 199,368 | 100.00% |
| `hit_landing_flat_hang_time_x` | 199,368 | 100.00% |
| `hit_landing_flat_confidence_x` | 199,368 | 100.00% |
| `hit_last_tracked_distance_x` | 199,368 | 100.00% |
| `hit_max_height_x` | 199,368 | 100.00% |
| `hit_flight_poly_fit_hit_trajectory_x_x` | 199,368 | 100.00% |
| `hit_flight_poly_fit_hit_trajectory_y_x` | 199,368 | 100.00% |
| `hit_flight_poly_fit_hit_trajectory_z_x` | 199,368 | 100.00% |
| `hit_launch_hit_spin_axis_x` | 199,368 | 100.00% |
| `hit_launch_hit_spin_rate_x` | 199,368 | 100.00% |
| `hit_position_at110_feet_x_x` | 199,368 | 100.00% |
| `hit_position_at110_feet_y_x` | 199,368 | 100.00% |
| `hit_position_at110_feet_z_x` | 199,368 | 100.00% |
| `hit_tracking_session_id` | 143,246 | 71.85% |
| `hit_tracking_source_endpoint` | 143,246 | 71.85% |
| `hit_tracking_source_file` | 143,246 | 71.85% |
| `hit_tracking_play_id` | 143,246 | 71.85% |
| `hit_tracking_track_id` | 143,246 | 71.85% |
| `hit_tracking_ball_match_key` | 143,246 | 71.85% |
| `hit_tracking_version` | 143,246 | 71.85% |
| `play_id_y` | 143,246 | 71.85% |
| `track_id_y` | 143,246 | 71.85% |
| `hit_tracking_track_start_time` | 143,246 | 71.85% |
| `hit_tracking_kind` | 143,246 | 71.85% |
| `pitch_release_rel_speed_y` | 199,368 | 100.00% |
| `pitch_release_spin_rate_y` | 199,368 | 100.00% |
| `pitch_release_extension_y` | 199,368 | 100.00% |
| `pitch_release_vert_rel_angle_y` | 199,368 | 100.00% |
| `pitch_release_horz_rel_angle_y` | 199,368 | 100.00% |
| `pitch_release_rel_height_y` | 199,368 | 100.00% |
| `pitch_release_rel_side_y` | 199,368 | 100.00% |
| `pitch_release_confidence_y` | 199,368 | 100.00% |
| `pitch_movement_horz_break_y` | 199,368 | 100.00% |
| `pitch_movement_vert_break_y` | 199,368 | 100.00% |
| `pitch_movement_induced_vert_break_y` | 199,368 | 100.00% |
| `pitch_movement_spin_axis_y` | 199,368 | 100.00% |
| `pitch_movement_tilt_y` | 199,368 | 100.00% |
| `pitch_movement_confidence_y` | 199,368 | 100.00% |
| `pitch_location_zone_time_y` | 199,368 | 100.00% |
| `pitch_location_plate_loc_height_y` | 199,368 | 100.00% |
| `pitch_location_plate_loc_side_y` | 199,368 | 100.00% |
| `pitch_location_zone_speed_y` | 199,368 | 100.00% |
| `pitch_location_vert_appr_angle_y` | 199,368 | 100.00% |
| `pitch_location_horz_appr_angle_y` | 199,368 | 100.00% |
| `pitch_location_confidence_y` | 199,368 | 100.00% |
| `pitch_nine_p_x0_x_y` | 199,368 | 100.00% |
| `pitch_nine_p_x0_y_y` | 199,368 | 100.00% |
| `pitch_nine_p_x0_z_y` | 199,368 | 100.00% |
| `pitch_nine_p_v0_x_y` | 199,368 | 100.00% |
| `pitch_nine_p_v0_y_y` | 199,368 | 100.00% |
| `pitch_nine_p_v0_z_y` | 199,368 | 100.00% |
| `pitch_nine_p_a0_x_y` | 199,368 | 100.00% |
| `pitch_nine_p_a0_y_y` | 199,368 | 100.00% |
| `pitch_nine_p_a0_z_y` | 199,368 | 100.00% |
| `pitch_nine_p_pfxx_y` | 199,368 | 100.00% |
| `pitch_nine_p_pfxz_y` | 199,368 | 100.00% |
| `pitch_speed_drop_y` | 199,368 | 100.00% |
| `pitch_flight_poly_fit_pitch_trajectory_x_y` | 199,368 | 100.00% |
| `pitch_flight_poly_fit_pitch_trajectory_y_y` | 199,368 | 100.00% |
| `pitch_flight_poly_fit_pitch_trajectory_z_y` | 199,368 | 100.00% |
| `pitch_effective_velo_y` | 199,368 | 100.00% |
| `catcher_throw_pop_time_y` | 199,368 | 100.00% |
| `catcher_throw_exchange_time_y` | 199,368 | 100.00% |
| `catcher_throw_catch_catch_position_x_y` | 199,368 | 100.00% |
| `catcher_throw_catch_catch_position_y_y` | 199,368 | 100.00% |
| `catcher_throw_catch_catch_position_z_y` | 199,368 | 100.00% |
| `catcher_throw_catch_confidence_y` | 199,368 | 100.00% |
| `catcher_throw_throw_throw_speed_y` | 199,368 | 100.00% |
| `catcher_throw_throw_throw_position_x_y` | 199,368 | 100.00% |
| `catcher_throw_throw_throw_position_y_y` | 199,368 | 100.00% |
| `catcher_throw_throw_throw_position_z_y` | 199,368 | 100.00% |
| `catcher_throw_location_time_to_base_y` | 199,368 | 100.00% |
| `catcher_throw_location_base_position_x_y` | 199,368 | 100.00% |
| `catcher_throw_location_base_position_y_y` | 199,368 | 100.00% |
| `catcher_throw_location_base_position_z_y` | 199,368 | 100.00% |
| `catcher_throw_location_confidence_y` | 199,368 | 100.00% |
| `catcher_throw_flight_poly_fit_throw_trajectory_x_y` | 199,368 | 100.00% |
| `catcher_throw_flight_poly_fit_throw_trajectory_y_y` | 199,368 | 100.00% |
| `catcher_throw_flight_poly_fit_throw_trajectory_z_y` | 199,368 | 100.00% |
| `hit_launch_exit_speed_y` | 143,246 | 71.85% |
| `hit_launch_contact_position_x_y` | 143,854 | 72.16% |
| `hit_launch_contact_position_y_y` | 143,854 | 72.16% |
| `hit_launch_contact_position_z_y` | 143,854 | 72.16% |
| `hit_launch_angle_y` | 143,246 | 71.85% |
| `hit_launch_direction_y` | 143,246 | 71.85% |
| `hit_launch_confidence_y` | 143,246 | 71.85% |
| `hit_landing_flat_distance_y` | 151,846 | 76.16% |
| `hit_landing_flat_bearing_y` | 151,846 | 76.16% |
| `hit_landing_flat_hang_time_y` | 151,846 | 76.16% |
| `hit_landing_flat_confidence_y` | 151,846 | 76.16% |
| `hit_last_tracked_distance_y` | 143,246 | 71.85% |
| `hit_max_height_y` | 143,246 | 71.85% |
| `hit_flight_poly_fit_hit_trajectory_x_y` | 143,246 | 71.85% |
| `hit_flight_poly_fit_hit_trajectory_y_y` | 143,246 | 71.85% |
| `hit_flight_poly_fit_hit_trajectory_z_y` | 143,246 | 71.85% |
| `hit_launch_hit_spin_axis_y` | 157,895 | 79.20% |
| `hit_launch_hit_spin_rate_y` | 159,008 | 79.76% |
| `hit_position_at110_feet_x_y` | 173,882 | 87.22% |
| `hit_position_at110_feet_y_y` | 173,882 | 87.22% |
| `hit_position_at110_feet_z_y` | 173,882 | 87.22% |
| `has_pitch_tracking` | 0 | 0.00% |
| `has_hit_tracking` | 0 | 0.00% |
| `has_any_tracking` | 0 | 0.00% |
| `pitch_tag_tagged_pitch_type_canonical` | 103,147 | 51.74% |
| `pitch_tag_auto_pitch_type_canonical` | 1,677 | 0.84% |
| `pitch_tag_pitch_call_canonical` | 3,608 | 1.81% |
| `hit_tag_tagged_hit_type_canonical` | 165,821 | 83.17% |
| `hit_tag_auto_hit_type_canonical` | 151,848 | 76.16% |
| `play_result_play_result_canonical` | 165,636 | 83.08% |
| `pitcher_throws_canonical` | 41 | 0.02% |
| `batter_side_canonical` | 172 | 0.09% |
| `catcher_throws_canonical` | 917 | 0.46% |
| `pitch_type` | 1,461 | 0.73% |
| `pitch_type_source` | 1,461 | 0.73% |
| `hit_type` | 149,572 | 75.02% |
| `hit_type_source` | 149,572 | 75.02% |
| `play_result` | 165,636 | 83.08% |
| `pitch_call` | 3,608 | 1.81% |
| `has_core_context` | 0 | 0.00% |
| `pitch_tracking_kind_normalized` | 1,651 | 0.83% |
| `hit_tracking_kind_normalized` | 143,246 | 71.85% |

## 4. Unique Values for Pitch Type Columns
### pitch_tag_tagged_pitch_type
dtype: `object` | missing: 0 | non-null unique values: 14
- `ChangeUp`
- `Curveball`
- `Cutter`
- `Fastball`
- `FourSeamFastBall`
- `Knuckleball`
- `OneSeamFastBall`
- `Other`
- `Sinker`
- `Slider`
- `Splitter`
- `Sweeper`
- `TwoSeamFastBall`
- `Undefined`

### pitch_tag_auto_pitch_type
dtype: `object` | missing: 1677 | non-null unique values: 8
- `Changeup`
- `Curveball`
- `Cutter`
- `Four-Seam`
- `Other`
- `Sinker`
- `Slider`
- `Splitter`

### pitch_tag_tagged_pitch_type_canonical
dtype: `string` | missing: 103147 | non-null unique values: 13
- `Changeup`
- `Curveball`
- `Cutter`
- `Fastball`
- `Four-Seam`
- `Knuckleball`
- `One Seam Fast Ball`
- `Other`
- `Sinker`
- `Slider`
- `Splitter`
- `Sweeper`
- `Two-Seam`

### pitch_tag_auto_pitch_type_canonical
dtype: `string` | missing: 1677 | non-null unique values: 8
- `Changeup`
- `Curveball`
- `Cutter`
- `Four-Seam`
- `Other`
- `Sinker`
- `Slider`
- `Splitter`

### pitch_type
dtype: `string` | missing: 1461 | non-null unique values: 13
- `Changeup`
- `Curveball`
- `Cutter`
- `Fastball`
- `Four-Seam`
- `Knuckleball`
- `One Seam Fast Ball`
- `Other`
- `Sinker`
- `Slider`
- `Splitter`
- `Sweeper`
- `Two-Seam`

### pitch_type_source
dtype: `string` | missing: 1461 | non-null unique values: 2
- `auto`
- `tagged`


## 5. Unique Values for Event/Outcome Columns
### kor_bb
dtype: `object` | missing: 0 | non-null unique values: 3
- `Strikeout`
- `Undefined`
- `Walk`

### pitch_tag_pitch_call
dtype: `object` | missing: 0 | non-null unique values: 12
- `AutomaticBall`
- `AutomaticStrike`
- `BallCalled`
- `BallIntentional`
- `BallinDirt`
- `FoulBallFieldable`
- `FoulBallNotFieldable`
- `HitByPitch`
- `InPlay`
- `StrikeCalled`
- `StrikeSwinging`
- `Undefined`

### hit_tag_tagged_hit_type
dtype: `object` | missing: 0 | non-null unique values: 6
- `Bunt`
- `FlyBall`
- `GroundBall`
- `LineDrive`
- `Popup`
- `Undefined`

### play_result_play_result
dtype: `object` | missing: 0 | non-null unique values: 12
- `CaughtStealing`
- `Double`
- `Error`
- `FieldersChoice`
- `HomeRun`
- `Out`
- `Sacrifice`
- `Single`
- `StolenBase`
- `Triple`
- `Undefined`
- `single`

### play_result_outs_on_play
dtype: `Int64` | missing: 0 | non-null unique values: 4
- `0`
- `1`
- `2`
- `3`

### play_result_runs_scored
dtype: `Int64` | missing: 0 | non-null unique values: 5
- `0`
- `1`
- `2`
- `3`
- `4`

### hit_tag_auto_hit_type
dtype: `object` | missing: 151848 | non-null unique values: 4
- `FlyBall`
- `GroundBall`
- `LineDrive`
- `Popup`

### strike_zone_decision
dtype: `object` | missing: 63926 | non-null unique values: 2
- `False`
- `True`

### pitch_tag_pitch_call_canonical
dtype: `string` | missing: 3608 | non-null unique values: 11
- `Automatic Ball`
- `Automatic Strike`
- `Ball Called`
- `Ball In Dirt`
- `Foul Ball Fieldable`
- `Foul Ball Not Fieldable`
- `Hit By Pitch`
- `In Play`
- `Intentional Ball`
- `Strike Called`
- `Strike Swinging`

### hit_tag_tagged_hit_type_canonical
dtype: `string` | missing: 165821 | non-null unique values: 5
- `Bunt`
- `Fly Ball`
- `Ground Ball`
- `Line Drive`
- `Pop Up`

### hit_tag_auto_hit_type_canonical
dtype: `string` | missing: 151848 | non-null unique values: 4
- `Fly Ball`
- `Ground Ball`
- `Line Drive`
- `Pop Up`

### play_result_play_result_canonical
dtype: `string` | missing: 165636 | non-null unique values: 10
- `Caught Stealing`
- `Double`
- `Error`
- `Fielder's Choice`
- `Home Run`
- `Out`
- `Sacrifice`
- `Single`
- `Stolen Base`
- `Triple`

### hit_type
dtype: `string` | missing: 149572 | non-null unique values: 5
- `Bunt`
- `Fly Ball`
- `Ground Ball`
- `Line Drive`
- `Pop Up`

### hit_type_source
dtype: `string` | missing: 149572 | non-null unique values: 2
- `auto`
- `tagged`

### play_result
dtype: `string` | missing: 165636 | non-null unique values: 10
- `Caught Stealing`
- `Double`
- `Error`
- `Fielder's Choice`
- `Home Run`
- `Out`
- `Sacrifice`
- `Single`
- `Stolen Base`
- `Triple`

### pitch_call
dtype: `string` | missing: 3608 | non-null unique values: 11
- `Automatic Ball`
- `Automatic Strike`
- `Ball Called`
- `Ball In Dirt`
- `Foul Ball Fieldable`
- `Foul Ball Not Fieldable`
- `Hit By Pitch`
- `In Play`
- `Intentional Ball`
- `Strike Called`
- `Strike Swinging`


## 6. Candidate Columns by Requested Field
These are name-based candidate matches using actual column names. They are not assumed canonical mappings.

| Requested Field | Candidate Column Names |
|---|---|
| Exit Velocity | `hit_launch_exit_speed_x`, `hit_launch_exit_speed_y` |
| Launch Angle | `hit_launch_angle_x`, `hit_launch_angle_y` |
| Spray Angle | `hit_launch_direction_x`, `hit_landing_flat_bearing_x`, `hit_launch_direction_y`, `hit_landing_flat_bearing_y` |
| Pitch Type | `pitch_tag_tagged_pitch_type`, `pitch_tag_auto_pitch_type`, `pitch_tag_tagged_pitch_type_canonical`, `pitch_tag_auto_pitch_type_canonical`, `pitch_type`, `pitch_type_source` |
| Pitcher Name | `pitcher_name` |
| Batter Name | `batter_name` |
| Plate Appearance Result | `kor_bb`, `play_result_play_result`, `play_result_outs_on_play`, `play_result_runs_scored`, `play_result_play_result_canonical`, `play_result` |
| Pitch Result | `pitch_tag_pitch_call`, `pitch_tag_pitch_call_canonical`, `pitch_call` |
| IVB | `pitch_movement_induced_vert_break_x`, `pitch_nine_p_pfxz_x`, `pitch_movement_induced_vert_break_y`, `pitch_nine_p_pfxz_y` |
| HB | `pitch_movement_horz_break_x`, `pitch_nine_p_pfxx_x`, `pitch_movement_horz_break_y`, `pitch_nine_p_pfxx_y` |
| Spin Rate | `pitch_release_spin_rate_x`, `hit_launch_hit_spin_rate_x`, `pitch_release_spin_rate_y`, `hit_launch_hit_spin_rate_y` |
| Velocity | `pitch_release_rel_speed_x`, `pitch_effective_velo_x`, `pitch_release_rel_speed_y`, `pitch_effective_velo_y` |

## 7. Dataset Structure Summary
The parquet file contains 199,368 rows and 242 columns. Column data types are distributed as follows:
- `Int64`: 8 columns
- `bool`: 4 columns
- `datetime64[ns, UTC]`: 1 columns
- `datetime64[ns]`: 1 columns
- `float64`: 123 columns
- `object`: 88 columns
- `string`: 17 columns

Columns with no missing values:
`session_id`, `source_endpoint`, `source_file`, `play_id`, `play_match_key`, `version`, `pitch_uid`, `kor_bb`, `tagger_behavior_pitch_no`, `pitcher_throws`, `pitcher_team`, `batter_team`, `catcher_throws`, `catcher_team`, `game_state_inning`, `game_state_top_bottom`, `game_state_outs`, `game_state_balls`, `game_state_strikes`, `pitch_tag_tagged_pitch_type`, `pitch_tag_pitch_call`, `hit_tag_tagged_hit_type`, `play_result_play_result`, `play_result_outs_on_play`, `play_result_runs_scored`, `has_pitch_tracking`, `has_hit_tracking`, `has_any_tracking`, `has_core_context`

Columns with all values missing:
`track_id`, `ball_match_key`, `catcher_throw_pop_time_x`, `catcher_throw_exchange_time_x`, `catcher_throw_catch_catch_position_x_x`, `catcher_throw_catch_catch_position_y_x`, `catcher_throw_catch_catch_position_z_x`, `catcher_throw_catch_confidence_x`, `catcher_throw_throw_throw_speed_x`, `catcher_throw_throw_throw_position_x_x`, `catcher_throw_throw_throw_position_y_x`, `catcher_throw_throw_throw_position_z_x`, `catcher_throw_location_time_to_base_x`, `catcher_throw_location_base_position_x_x`, `catcher_throw_location_base_position_y_x`, `catcher_throw_location_base_position_z_x`, `catcher_throw_location_confidence_x`, `catcher_throw_flight_poly_fit_throw_trajectory_x_x`, `catcher_throw_flight_poly_fit_throw_trajectory_y_x`, `catcher_throw_flight_poly_fit_throw_trajectory_z_x`, `hit_launch_exit_speed_x`, `hit_launch_contact_position_x_x`, `hit_launch_contact_position_y_x`, `hit_launch_contact_position_z_x`, `hit_launch_angle_x`, `hit_launch_direction_x`, `hit_launch_confidence_x`, `hit_landing_flat_distance_x`, `hit_landing_flat_bearing_x`, `hit_landing_flat_hang_time_x`, `hit_landing_flat_confidence_x`, `hit_last_tracked_distance_x`, `hit_max_height_x`, `hit_flight_poly_fit_hit_trajectory_x_x`, `hit_flight_poly_fit_hit_trajectory_y_x`, `hit_flight_poly_fit_hit_trajectory_z_x`, `hit_launch_hit_spin_axis_x`, `hit_launch_hit_spin_rate_x`, `hit_position_at110_feet_x_x`, `hit_position_at110_feet_y_x`, `hit_position_at110_feet_z_x`, `pitch_release_rel_speed_y`, `pitch_release_spin_rate_y`, `pitch_release_extension_y`, `pitch_release_vert_rel_angle_y`, `pitch_release_horz_rel_angle_y`, `pitch_release_rel_height_y`, `pitch_release_rel_side_y`, `pitch_release_confidence_y`, `pitch_movement_horz_break_y`, `pitch_movement_vert_break_y`, `pitch_movement_induced_vert_break_y`, `pitch_movement_spin_axis_y`, `pitch_movement_tilt_y`, `pitch_movement_confidence_y`, `pitch_location_zone_time_y`, `pitch_location_plate_loc_height_y`, `pitch_location_plate_loc_side_y`, `pitch_location_zone_speed_y`, `pitch_location_vert_appr_angle_y`, `pitch_location_horz_appr_angle_y`, `pitch_location_confidence_y`, `pitch_nine_p_x0_x_y`, `pitch_nine_p_x0_y_y`, `pitch_nine_p_x0_z_y`, `pitch_nine_p_v0_x_y`, `pitch_nine_p_v0_y_y`, `pitch_nine_p_v0_z_y`, `pitch_nine_p_a0_x_y`, `pitch_nine_p_a0_y_y`, `pitch_nine_p_a0_z_y`, `pitch_nine_p_pfxx_y`, `pitch_nine_p_pfxz_y`, `pitch_speed_drop_y`, `pitch_flight_poly_fit_pitch_trajectory_x_y`, `pitch_flight_poly_fit_pitch_trajectory_y_y`, `pitch_flight_poly_fit_pitch_trajectory_z_y`, `pitch_effective_velo_y`, `catcher_throw_pop_time_y`, `catcher_throw_exchange_time_y`, `catcher_throw_catch_catch_position_x_y`, `catcher_throw_catch_catch_position_y_y`, `catcher_throw_catch_catch_position_z_y`, `catcher_throw_catch_confidence_y`, `catcher_throw_throw_throw_speed_y`, `catcher_throw_throw_throw_position_x_y`, `catcher_throw_throw_throw_position_y_y`, `catcher_throw_throw_throw_position_z_y`, `catcher_throw_location_time_to_base_y`, `catcher_throw_location_base_position_x_y`, `catcher_throw_location_base_position_y_y`, `catcher_throw_location_base_position_z_y`, `catcher_throw_location_confidence_y`, `catcher_throw_flight_poly_fit_throw_trajectory_x_y`, `catcher_throw_flight_poly_fit_throw_trajectory_y_y`, `catcher_throw_flight_poly_fit_throw_trajectory_z_y`

Highest-missing columns:
- `ball_match_key`: 199,368 missing (100.00%)
- `track_id`: 199,368 missing (100.00%)
- `catcher_throw_flight_poly_fit_throw_trajectory_z_x`: 199,368 missing (100.00%)
- `catcher_throw_flight_poly_fit_throw_trajectory_y_x`: 199,368 missing (100.00%)
- `hit_launch_exit_speed_x`: 199,368 missing (100.00%)
- `catcher_throw_flight_poly_fit_throw_trajectory_x_x`: 199,368 missing (100.00%)
- `catcher_throw_location_confidence_x`: 199,368 missing (100.00%)
- `catcher_throw_location_base_position_z_x`: 199,368 missing (100.00%)
- `catcher_throw_location_base_position_y_x`: 199,368 missing (100.00%)
- `catcher_throw_location_base_position_x_x`: 199,368 missing (100.00%)
- `catcher_throw_location_time_to_base_x`: 199,368 missing (100.00%)
- `catcher_throw_throw_throw_position_z_x`: 199,368 missing (100.00%)
- `catcher_throw_throw_throw_position_y_x`: 199,368 missing (100.00%)
- `catcher_throw_throw_throw_position_x_x`: 199,368 missing (100.00%)
- `catcher_throw_throw_throw_speed_x`: 199,368 missing (100.00%)
- `catcher_throw_catch_confidence_x`: 199,368 missing (100.00%)
- `catcher_throw_catch_catch_position_z_x`: 199,368 missing (100.00%)
- `catcher_throw_catch_catch_position_y_x`: 199,368 missing (100.00%)
- `catcher_throw_exchange_time_x`: 199,368 missing (100.00%)
- `catcher_throw_catch_catch_position_x_x`: 199,368 missing (100.00%)

Lowest-missing columns:
- `session_id`: 0 missing (0.00%)
- `source_endpoint`: 0 missing (0.00%)
- `source_file`: 0 missing (0.00%)
- `play_id`: 0 missing (0.00%)
- `play_match_key`: 0 missing (0.00%)
- `version`: 0 missing (0.00%)
- `kor_bb`: 0 missing (0.00%)
- `pitch_uid`: 0 missing (0.00%)
- `tagger_behavior_pitch_no`: 0 missing (0.00%)
- `catcher_throws`: 0 missing (0.00%)
- `game_state_top_bottom`: 0 missing (0.00%)
- `game_state_inning`: 0 missing (0.00%)
- `game_state_outs`: 0 missing (0.00%)
- `batter_team`: 0 missing (0.00%)
- `pitcher_throws`: 0 missing (0.00%)
- `pitcher_team`: 0 missing (0.00%)
- `game_state_balls`: 0 missing (0.00%)
- `catcher_team`: 0 missing (0.00%)
- `play_result_play_result`: 0 missing (0.00%)
- `play_result_outs_on_play`: 0 missing (0.00%)

Numeric column count: 131
Non-numeric column count: 111