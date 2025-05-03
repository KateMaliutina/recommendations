
COPY public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) FROM stdin;
1	7	53	\N	f
2	7	54	1	f
3	7	55	1	f
4	7	56	\N	f
5	7	5	4	t
6	7	8	4	t
7	7	41	4	t
8	7	44	4	t
9	7	57	4	t
10	7	58	4	t
11	7	59	4	t
12	7	60	4	t
13	7	61	\N	f
14	7	10	13	f
15	7	20	13	t
16	7	62	13	t
17	7	95	\N	f
18	7	63	17	t
19	7	64	17	t
20	7	43	17	t
21	7	39	\N	f
22	7	65	21	f
23	7	66	21	f
24	7	67	21	f
25	7	68	21	f
26	7	69	21	f
27	7	70	21	t
28	7	71	21	t
29	7	72	21	t
30	7	73	21	t
31	7	75	\N	f
32	7	74	31	t
33	7	48	31	f
34	7	76	31	t
35	7	77	31	t
36	7	78	\N	t
37	7	79	36	t
38	7	80	36	t
39	7	81	36	t
40	7	101	36	t
41	7	102	36	t
42	7	103	36	t
43	7	104	36	t
44	7	82	\N	f
45	7	83	44	t
46	7	84	44	f
47	7	85	44	f
48	7	86	\N	f
49	7	87	48	f
50	7	88	48	t
51	7	133	\N	t
52	7	89	51	f
53	7	90	51	f
54	7	91	51	f
55	7	92	51	f
56	7	93	51	f
57	7	94	51	t
58	7	96	51	f
59	7	100	\N	t
60	7	97	59	t
61	7	98	59	t
62	7	99	59	t
63	7	134	\N	f
64	7	49	63	f
65	7	50	63	t
66	7	51	63	t
67	7	105	\N	f
68	7	106	67	f
69	7	107	67	f
70	7	108	67	f
71	7	109	67	f
72	7	110	\N	f
73	7	111	72	t
74	7	112	72	t
75	7	47	72	t
76	7	131	\N	t
77	7	113	76	t
78	7	114	76	t
79	7	115	76	t
80	7	116	76	t
81	7	117	\N	f
82	7	118	81	f
83	7	119	81	t
84	7	120	\N	f
85	7	121	84	f
86	7	122	\N	f
87	7	123	86	t
88	7	124	86	t
89	7	125	86	t
90	7	48	86	t
91	7	135	\N	t
92	7	126	91	t
93	7	127	91	t
94	7	128	91	t
95	7	129	91	t
96	7	130	91	t
97	7	132	91	t
\.


--
-- Data for Name: roadmaps; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roadmaps (id, specialization, grade) FROM stdin;
1	qa	intern
2	qa	junior
3	ios	intern
4	ios	junior
5	android	intern
6	android	junior
7	backend	intern
8	backend	junior
9	frontend	intern
10	frontend	junior
11	fullstack	intern
12	fullstack	junior
13	product manager	intern
14	product manager	junior
15	project manager	intern
16	project manager	junior
17	game developer	intern
18	game developer	junior
19	devops	intern
20	devops	junior
21	ux/ui designer	intern
22	ux/ui designer	junior
23	data scientist	intern
24	data scientist	junior
\.


--
-- Data for Name: skills; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.skills (id, name) FROM stdin;
1	str1ing
2	string
3	react
4	redux
5	typescript
6	css3
7	vue
8	javascript
9	html5
10	git
12	алгоритмы и структуры данных
13	графы
14	граф
15	d3.js
16	three.js
17	networkx
18	graph-tool
19	pygraphvis
20	github
21	sass
22	es6
23	html
24	zustand
25	nuxt
26	tailwindcss
27	strapi
28	cms wordpress
29	modx
30	ext js
31	работа с большим объемом информации
32	деловая переписка
33	webpack
34	решение проблем
35	ответственность
36	грамотная устная речь
37	пользователь пк
38	css
39	api
40	gulp
41	c#
42	asp.net
43	postgresql
44	php
45	yii2
46	rest api
47	rabbitmq
48	redis
49	docker
50	kubernetes
51	helm
52	laravel
53	интернет
54	http
55	dns
56	языки программирования
57	go
58	python
59	java
60	rust
61	системы контроля версий
62	gitlab
63	sqlite
64	mysql
65	jwt
66	oauth
67	cookie
68	rest
69	json
70	grpc
71	graphql
72	soap
73	xml
74	memcached
75	кэширование
76	cdn
77	кэширование на стороне клиента
78	безопасность
79	sha
80	bcrypt
81	md5
82	тестирование
83	интеграционное
84	unit
85	функциональное
86	ci/cd
87	github actions
88	jenkins
89	orm
90	acid
91	транзакции
92	нормализация
93	миграции
94	n+1 проблема
95	базы данных
96	индексы
97	репликация
98	шардирование
99	cap теорема
100	масштабирование
101	https
102	cors
103	ssl/tls
104	sql инъекции
105	архитектурные паттерны
106	монолит
107	микросервисы
108	stateless
109	statefull
110	брокеры сообщений
111	kafka
112	nats
113	elk стек
114	elasticsearch
115	grafana
116	kibana
117	балансировщики нагрузки
118	nginx
119	haproxy
120	общение в режиме реального времени
121	websockets
122	nosql базы данных
123	mongodb
124	cassandra
125	firebase
126	graceful degradation
127	throttling
128	loadshifting
129	backpressure
130	circuit breaker
131	observability
132	мониторинг
133	базы данных углубленно
134	контейнеризация и виртуализация
135	дальнейшее масштабирование
\.


--
-- Name: roadmap_nodes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roadmap_nodes_id_seq', 97, true);


--
-- Name: roadmaps_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roadmaps_id_seq', 24, true);


--
-- Name: skills_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.skills_id_seq', 135, true);