--
-- PostgreSQL database dump
--

-- Dumped from database version 17.3 (Debian 17.3-3.pgdg120+1)
-- Dumped by pg_dump version 17.4 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: recommendations; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE recommendations WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE recommendations OWNER TO postgres;

\connect recommendations

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: skillstatus; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.skillstatus AS ENUM (
    'not_started',
    'in_progress',
    'learned'
);


ALTER TYPE public.skillstatus OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: recommendations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recommendations (
    id integer NOT NULL,
    user_id integer,
    vacancy_id integer,
    score integer NOT NULL
);


ALTER TABLE public.recommendations OWNER TO postgres;

--
-- Name: recommendations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recommendations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.recommendations_id_seq OWNER TO postgres;

--
-- Name: recommendations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recommendations_id_seq OWNED BY public.recommendations.id;


--
-- Name: roadmap_nodes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roadmap_nodes (
    id integer NOT NULL,
    roadmap_id integer NOT NULL,
    skill_id integer NOT NULL,
    parent_id integer,
    is_optional boolean
);


ALTER TABLE public.roadmap_nodes OWNER TO postgres;

--
-- Name: roadmap_nodes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roadmap_nodes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.roadmap_nodes_id_seq OWNER TO postgres;

--
-- Name: roadmap_nodes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.roadmap_nodes_id_seq OWNED BY public.roadmap_nodes.id;


--
-- Name: roadmaps; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roadmaps (
    id integer NOT NULL,
    specialization character varying NOT NULL,
    grade character varying NOT NULL
);


ALTER TABLE public.roadmaps OWNER TO postgres;

--
-- Name: roadmaps_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roadmaps_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.roadmaps_id_seq OWNER TO postgres;

--
-- Name: roadmaps_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.roadmaps_id_seq OWNED BY public.roadmaps.id;


--
-- Name: skills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.skills (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.skills OWNER TO postgres;

--
-- Name: skills_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.skills_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.skills_id_seq OWNER TO postgres;

--
-- Name: skills_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.skills_id_seq OWNED BY public.skills.id;


--
-- Name: user_roadmap_nodes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_roadmap_nodes (
    id integer NOT NULL,
    user_id integer NOT NULL,
    roadmap_node_id integer NOT NULL,
    status public.skillstatus NOT NULL
);


ALTER TABLE public.user_roadmap_nodes OWNER TO postgres;

--
-- Name: user_roadmap_nodes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_roadmap_nodes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_roadmap_nodes_id_seq OWNER TO postgres;

--
-- Name: user_roadmap_nodes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_roadmap_nodes_id_seq OWNED BY public.user_roadmap_nodes.id;


--
-- Name: user_skills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_skills (
    user_id integer NOT NULL,
    skill_id integer NOT NULL,
    proficiency_level integer NOT NULL
);


ALTER TABLE public.user_skills OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying,
    email character varying NOT NULL,
    interests character varying[],
    grade character varying
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: vacancies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vacancies (
    id integer NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    grade character varying NOT NULL,
    employer_name character varying NOT NULL,
    url character varying NOT NULL
);


ALTER TABLE public.vacancies OWNER TO postgres;

--
-- Name: vacancies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vacancies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vacancies_id_seq OWNER TO postgres;

--
-- Name: vacancies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vacancies_id_seq OWNED BY public.vacancies.id;


--
-- Name: vacancy_skills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vacancy_skills (
    vacancy_id integer NOT NULL,
    skill_id integer NOT NULL
);


ALTER TABLE public.vacancy_skills OWNER TO postgres;

--
-- Name: recommendations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations ALTER COLUMN id SET DEFAULT nextval('public.recommendations_id_seq'::regclass);


--
-- Name: roadmap_nodes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roadmap_nodes ALTER COLUMN id SET DEFAULT nextval('public.roadmap_nodes_id_seq'::regclass);


--
-- Name: roadmaps id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roadmaps ALTER COLUMN id SET DEFAULT nextval('public.roadmaps_id_seq'::regclass);


--
-- Name: skills id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills ALTER COLUMN id SET DEFAULT nextval('public.skills_id_seq'::regclass);


--
-- Name: user_roadmap_nodes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roadmap_nodes ALTER COLUMN id SET DEFAULT nextval('public.user_roadmap_nodes_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: vacancies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacancies ALTER COLUMN id SET DEFAULT nextval('public.vacancies_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
8d12800405b0
\.


--
-- Data for Name: recommendations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recommendations (id, user_id, vacancy_id, score) FROM stdin;
\.


--
-- Data for Name: roadmap_nodes; Type: TABLE DATA; Schema: public; Owner: postgres
--

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
-- Data for Name: user_roadmap_nodes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_roadmap_nodes (id, user_id, roadmap_node_id, status) FROM stdin;
\.


--
-- Data for Name: user_skills; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_skills (user_id, skill_id, proficiency_level) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, email, interests, grade) FROM stdin;
\.


--
-- Data for Name: vacancies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vacancies (id, title, description, grade, employer_name, url) FROM stdin;
\.


--
-- Data for Name: vacancy_skills; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vacancy_skills (vacancy_id, skill_id) FROM stdin;
\.


--
-- Name: recommendations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recommendations_id_seq', 1, false);


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


--
-- Name: user_roadmap_nodes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_roadmap_nodes_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


--
-- Name: vacancies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vacancies_id_seq', 20, true);


--
-- Name: roadmaps _specialization_grade_uc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roadmaps
    ADD CONSTRAINT _specialization_grade_uc UNIQUE (specialization, grade);


--
-- Name: user_roadmap_nodes _user_node_uc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roadmap_nodes
    ADD CONSTRAINT _user_node_uc UNIQUE (user_id, roadmap_node_id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: recommendations recommendations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations
    ADD CONSTRAINT recommendations_pkey PRIMARY KEY (id);


--
-- Name: roadmap_nodes roadmap_nodes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roadmap_nodes
    ADD CONSTRAINT roadmap_nodes_pkey PRIMARY KEY (id);


--
-- Name: roadmaps roadmaps_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roadmaps
    ADD CONSTRAINT roadmaps_pkey PRIMARY KEY (id);


--
-- Name: skills skills_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills
    ADD CONSTRAINT skills_name_key UNIQUE (name);


--
-- Name: skills skills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills
    ADD CONSTRAINT skills_pkey PRIMARY KEY (id);


--
-- Name: user_roadmap_nodes user_roadmap_nodes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roadmap_nodes
    ADD CONSTRAINT user_roadmap_nodes_pkey PRIMARY KEY (id);


--
-- Name: user_skills user_skills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_skills
    ADD CONSTRAINT user_skills_pkey PRIMARY KEY (user_id, skill_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: vacancies vacancies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacancies
    ADD CONSTRAINT vacancies_pkey PRIMARY KEY (id);


--
-- Name: vacancy_skills vacancy_skills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacancy_skills
    ADD CONSTRAINT vacancy_skills_pkey PRIMARY KEY (vacancy_id, skill_id);


--
-- Name: ix_recommendations_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_recommendations_id ON public.recommendations USING btree (id);


--
-- Name: ix_roadmap_nodes_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_roadmap_nodes_id ON public.roadmap_nodes USING btree (id);


--
-- Name: ix_roadmaps_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_roadmaps_id ON public.roadmaps USING btree (id);


--
-- Name: ix_skills_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_skills_id ON public.skills USING btree (id);


--
-- Name: ix_user_roadmap_nodes_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_user_roadmap_nodes_id ON public.user_roadmap_nodes USING btree (id);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: ix_vacancies_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_vacancies_id ON public.vacancies USING btree (id);


--
-- Name: recommendations recommendations_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations
    ADD CONSTRAINT recommendations_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: recommendations recommendations_vacancy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations
    ADD CONSTRAINT recommendations_vacancy_id_fkey FOREIGN KEY (vacancy_id) REFERENCES public.vacancies(id);


--
-- Name: roadmap_nodes roadmap_nodes_parent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roadmap_nodes
    ADD CONSTRAINT roadmap_nodes_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES public.roadmap_nodes(id);


--
-- Name: roadmap_nodes roadmap_nodes_roadmap_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roadmap_nodes
    ADD CONSTRAINT roadmap_nodes_roadmap_id_fkey FOREIGN KEY (roadmap_id) REFERENCES public.roadmaps(id);


--
-- Name: roadmap_nodes roadmap_nodes_skill_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roadmap_nodes
    ADD CONSTRAINT roadmap_nodes_skill_id_fkey FOREIGN KEY (skill_id) REFERENCES public.skills(id);


--
-- Name: user_roadmap_nodes user_roadmap_nodes_roadmap_node_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roadmap_nodes
    ADD CONSTRAINT user_roadmap_nodes_roadmap_node_id_fkey FOREIGN KEY (roadmap_node_id) REFERENCES public.roadmap_nodes(id);


--
-- Name: user_roadmap_nodes user_roadmap_nodes_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_roadmap_nodes
    ADD CONSTRAINT user_roadmap_nodes_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: user_skills user_skills_skill_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_skills
    ADD CONSTRAINT user_skills_skill_id_fkey FOREIGN KEY (skill_id) REFERENCES public.skills(id);


--
-- Name: user_skills user_skills_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_skills
    ADD CONSTRAINT user_skills_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: vacancy_skills vacancy_skills_skill_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacancy_skills
    ADD CONSTRAINT vacancy_skills_skill_id_fkey FOREIGN KEY (skill_id) REFERENCES public.skills(id);


--
-- Name: vacancy_skills vacancy_skills_vacancy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacancy_skills
    ADD CONSTRAINT vacancy_skills_vacancy_id_fkey FOREIGN KEY (vacancy_id) REFERENCES public.vacancies(id);


--
-- PostgreSQL database dump complete
--

