"""add initial data

Revision ID: c00adf1ec998
Revises: 8d12800405b0
Create Date: 2025-05-04 16:34:50.732153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c00adf1ec998'
down_revision: Union[str, None] = '8d12800405b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
--
-- Data for Name: roadmaps; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.roadmaps (id, specialization, grade) VALUES (1, 'qa', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (2, 'qa', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (3, 'ios', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (4, 'ios', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (5, 'android', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (6, 'android', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (7, 'backend', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (8, 'backend', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (9, 'frontend', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (10, 'frontend', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (11, 'fullstack', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (12, 'fullstack', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (13, 'product manager', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (14, 'product manager', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (15, 'project manager', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (16, 'project manager', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (17, 'game developer', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (18, 'game developer', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (19, 'devops', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (20, 'devops', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (21, 'ux/ui designer', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (22, 'ux/ui designer', 'junior');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (23, 'data scientist', 'intern');
INSERT INTO public.roadmaps (id, specialization, grade) VALUES (24, 'data scientist', 'junior');

--
-- Data for Name: skills; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.skills (id, name) VALUES (3, 'react');
INSERT INTO public.skills (id, name) VALUES (4, 'redux');
INSERT INTO public.skills (id, name) VALUES (5, 'typescript');
INSERT INTO public.skills (id, name) VALUES (7, 'vue');
INSERT INTO public.skills (id, name) VALUES (8, 'javascript');
INSERT INTO public.skills (id, name) VALUES (10, 'git');
INSERT INTO public.skills (id, name) VALUES (12, 'алгоритмы и структуры данных');
INSERT INTO public.skills (id, name) VALUES (13, 'графы');
INSERT INTO public.skills (id, name) VALUES (14, 'граф');
INSERT INTO public.skills (id, name) VALUES (15, 'd3.js');
INSERT INTO public.skills (id, name) VALUES (16, 'three.js');
INSERT INTO public.skills (id, name) VALUES (17, 'networkx');
INSERT INTO public.skills (id, name) VALUES (18, 'graph-tool');
INSERT INTO public.skills (id, name) VALUES (19, 'pygraphvis');
INSERT INTO public.skills (id, name) VALUES (20, 'github');
INSERT INTO public.skills (id, name) VALUES (21, 'sass');
INSERT INTO public.skills (id, name) VALUES (22, 'es6');
INSERT INTO public.skills (id, name) VALUES (23, 'html');
INSERT INTO public.skills (id, name) VALUES (24, 'zustand');
INSERT INTO public.skills (id, name) VALUES (25, 'nuxt');
INSERT INTO public.skills (id, name) VALUES (27, 'strapi');
INSERT INTO public.skills (id, name) VALUES (28, 'cms wordpress');
INSERT INTO public.skills (id, name) VALUES (29, 'modx');
INSERT INTO public.skills (id, name) VALUES (30, 'ext js');
INSERT INTO public.skills (id, name) VALUES (31, 'работа с большим объемом информации');
INSERT INTO public.skills (id, name) VALUES (32, 'деловая переписка');
INSERT INTO public.skills (id, name) VALUES (33, 'webpack');
INSERT INTO public.skills (id, name) VALUES (34, 'решение проблем');
INSERT INTO public.skills (id, name) VALUES (35, 'ответственность');
INSERT INTO public.skills (id, name) VALUES (36, 'грамотная устная речь');
INSERT INTO public.skills (id, name) VALUES (37, 'пользователь пк');
INSERT INTO public.skills (id, name) VALUES (38, 'css');
INSERT INTO public.skills (id, name) VALUES (39, 'api');
INSERT INTO public.skills (id, name) VALUES (40, 'gulp');
INSERT INTO public.skills (id, name) VALUES (41, 'c#');
INSERT INTO public.skills (id, name) VALUES (42, 'asp.net');
INSERT INTO public.skills (id, name) VALUES (43, 'postgresql');
INSERT INTO public.skills (id, name) VALUES (44, 'php');
INSERT INTO public.skills (id, name) VALUES (45, 'yii2');
INSERT INTO public.skills (id, name) VALUES (46, 'rest api');
INSERT INTO public.skills (id, name) VALUES (47, 'rabbitmq');
INSERT INTO public.skills (id, name) VALUES (48, 'redis');
INSERT INTO public.skills (id, name) VALUES (49, 'docker');
INSERT INTO public.skills (id, name) VALUES (50, 'kubernetes');
INSERT INTO public.skills (id, name) VALUES (51, 'helm');
INSERT INTO public.skills (id, name) VALUES (52, 'laravel');
INSERT INTO public.skills (id, name) VALUES (53, 'интернет');
INSERT INTO public.skills (id, name) VALUES (54, 'http');
INSERT INTO public.skills (id, name) VALUES (55, 'dns');
INSERT INTO public.skills (id, name) VALUES (56, 'языки программирования');
INSERT INTO public.skills (id, name) VALUES (57, 'go');
INSERT INTO public.skills (id, name) VALUES (58, 'python');
INSERT INTO public.skills (id, name) VALUES (59, 'java');
INSERT INTO public.skills (id, name) VALUES (60, 'rust');
INSERT INTO public.skills (id, name) VALUES (61, 'системы контроля версий');
INSERT INTO public.skills (id, name) VALUES (62, 'gitlab');
INSERT INTO public.skills (id, name) VALUES (63, 'sqlite');
INSERT INTO public.skills (id, name) VALUES (64, 'mysql');
INSERT INTO public.skills (id, name) VALUES (65, 'jwt');
INSERT INTO public.skills (id, name) VALUES (66, 'oauth');
INSERT INTO public.skills (id, name) VALUES (67, 'cookie');
INSERT INTO public.skills (id, name) VALUES (68, 'rest');
INSERT INTO public.skills (id, name) VALUES (69, 'json');
INSERT INTO public.skills (id, name) VALUES (70, 'grpc');
INSERT INTO public.skills (id, name) VALUES (71, 'graphql');
INSERT INTO public.skills (id, name) VALUES (72, 'soap');
INSERT INTO public.skills (id, name) VALUES (73, 'xml');
INSERT INTO public.skills (id, name) VALUES (74, 'memcached');
INSERT INTO public.skills (id, name) VALUES (75, 'кэширование');
INSERT INTO public.skills (id, name) VALUES (76, 'cdn');
INSERT INTO public.skills (id, name) VALUES (77, 'кэширование на стороне клиента');
INSERT INTO public.skills (id, name) VALUES (78, 'безопасность');
INSERT INTO public.skills (id, name) VALUES (79, 'sha');
INSERT INTO public.skills (id, name) VALUES (80, 'bcrypt');
INSERT INTO public.skills (id, name) VALUES (81, 'md5');
INSERT INTO public.skills (id, name) VALUES (82, 'тестирование');
INSERT INTO public.skills (id, name) VALUES (83, 'интеграционное');
INSERT INTO public.skills (id, name) VALUES (84, 'unit');
INSERT INTO public.skills (id, name) VALUES (85, 'функциональное');
INSERT INTO public.skills (id, name) VALUES (86, 'ci/cd');
INSERT INTO public.skills (id, name) VALUES (87, 'github actions');
INSERT INTO public.skills (id, name) VALUES (88, 'jenkins');
INSERT INTO public.skills (id, name) VALUES (89, 'orm');
INSERT INTO public.skills (id, name) VALUES (90, 'acid');
INSERT INTO public.skills (id, name) VALUES (91, 'транзакции');
INSERT INTO public.skills (id, name) VALUES (92, 'нормализация');
INSERT INTO public.skills (id, name) VALUES (93, 'миграции');
INSERT INTO public.skills (id, name) VALUES (94, 'n+1 проблема');
INSERT INTO public.skills (id, name) VALUES (95, 'базы данных');
INSERT INTO public.skills (id, name) VALUES (96, 'индексы');
INSERT INTO public.skills (id, name) VALUES (97, 'репликация');
INSERT INTO public.skills (id, name) VALUES (98, 'шардирование');
INSERT INTO public.skills (id, name) VALUES (99, 'cap теорема');
INSERT INTO public.skills (id, name) VALUES (100, 'масштабирование');
INSERT INTO public.skills (id, name) VALUES (101, 'https');
INSERT INTO public.skills (id, name) VALUES (102, 'cors');
INSERT INTO public.skills (id, name) VALUES (103, 'ssl/tls');
INSERT INTO public.skills (id, name) VALUES (104, 'sql инъекции');
INSERT INTO public.skills (id, name) VALUES (105, 'архитектурные паттерны');
INSERT INTO public.skills (id, name) VALUES (106, 'монолит');
INSERT INTO public.skills (id, name) VALUES (107, 'микросервисы');
INSERT INTO public.skills (id, name) VALUES (108, 'stateless');
INSERT INTO public.skills (id, name) VALUES (109, 'statefull');
INSERT INTO public.skills (id, name) VALUES (110, 'брокеры сообщений');
INSERT INTO public.skills (id, name) VALUES (111, 'kafka');
INSERT INTO public.skills (id, name) VALUES (112, 'nats');
INSERT INTO public.skills (id, name) VALUES (113, 'elk стек');
INSERT INTO public.skills (id, name) VALUES (114, 'elasticsearch');
INSERT INTO public.skills (id, name) VALUES (115, 'grafana');
INSERT INTO public.skills (id, name) VALUES (116, 'kibana');
INSERT INTO public.skills (id, name) VALUES (117, 'балансировщики нагрузки');
INSERT INTO public.skills (id, name) VALUES (118, 'nginx');
INSERT INTO public.skills (id, name) VALUES (119, 'haproxy');
INSERT INTO public.skills (id, name) VALUES (120, 'общение в режиме реального времени');
INSERT INTO public.skills (id, name) VALUES (121, 'websockets');
INSERT INTO public.skills (id, name) VALUES (122, 'nosql базы данных');
INSERT INTO public.skills (id, name) VALUES (123, 'mongodb');
INSERT INTO public.skills (id, name) VALUES (124, 'cassandra');
INSERT INTO public.skills (id, name) VALUES (125, 'firebase');
INSERT INTO public.skills (id, name) VALUES (126, 'graceful degradation');
INSERT INTO public.skills (id, name) VALUES (127, 'throttling');
INSERT INTO public.skills (id, name) VALUES (128, 'loadshifting');
INSERT INTO public.skills (id, name) VALUES (129, 'backpressure');
INSERT INTO public.skills (id, name) VALUES (130, 'circuit breaker');
INSERT INTO public.skills (id, name) VALUES (131, 'observability');
INSERT INTO public.skills (id, name) VALUES (132, 'мониторинг');
INSERT INTO public.skills (id, name) VALUES (133, 'базы данных углубленно');
INSERT INTO public.skills (id, name) VALUES (134, 'контейнеризация и виртуализация');
INSERT INTO public.skills (id, name) VALUES (135, 'дальнейшее масштабирование');
INSERT INTO public.skills (id, name) VALUES (136, 'dom');
INSERT INTO public.skills (id, name) VALUES (137, 'пакетные менеджеры');
INSERT INTO public.skills (id, name) VALUES (138, 'yarn');
INSERT INTO public.skills (id, name) VALUES (139, 'npm');
INSERT INTO public.skills (id, name) VALUES (140, 'framework');
INSERT INTO public.skills (id, name) VALUES (141, 'angular');
INSERT INTO public.skills (id, name) VALUES (142, 'next');
INSERT INTO public.skills (id, name) VALUES (26, 'tailwind');
INSERT INTO public.skills (id, name) VALUES (143, 'средства сборки');
INSERT INTO public.skills (id, name) VALUES (144, 'prettier');
INSERT INTO public.skills (id, name) VALUES (145, 'eslint');
INSERT INTO public.skills (id, name) VALUES (146, 'module bundlers');
INSERT INTO public.skills (id, name) VALUES (147, 'vite');
INSERT INTO public.skills (id, name) VALUES (148, 'esbuild');
INSERT INTO public.skills (id, name) VALUES (149, 'линтеры');
INSERT INTO public.skills (id, name) VALUES (150, 'vitest');
INSERT INTO public.skills (id, name) VALUES (151, 'jest');
INSERT INTO public.skills (id, name) VALUES (152, 'playwright');
INSERT INTO public.skills (id, name) VALUES (153, 'cypress');
INSERT INTO public.skills (id, name) VALUES (154, 'pwa');
INSERT INTO public.skills (id, name) VALUES (155, 'astro');
INSERT INTO public.skills (id, name) VALUES (156, 'kotlin');
INSERT INTO public.skills (id, name) VALUES (157, 'ооп');
INSERT INTO public.skills (id, name) VALUES (158, 'android studio');
INSERT INTO public.skills (id, name) VALUES (159, 'основы');
INSERT INTO public.skills (id, name) VALUES (160, 'компоненты приложения');
INSERT INTO public.skills (id, name) VALUES (161, 'activity');
INSERT INTO public.skills (id, name) VALUES (162, 'activity lifecycle');
INSERT INTO public.skills (id, name) VALUES (163, 'изменения state');
INSERT INTO public.skills (id, name) VALUES (164, 'task');
INSERT INTO public.skills (id, name) VALUES (165, 'fragment');
INSERT INTO public.skills (id, name) VALUES (166, 'intent');
INSERT INTO public.skills (id, name) VALUES (167, 'явные');
INSERT INTO public.skills (id, name) VALUES (168, 'неявные');
INSERT INTO public.skills (id, name) VALUES (169, 'intent filter');
INSERT INTO public.skills (id, name) VALUES (170, 'services');
INSERT INTO public.skills (id, name) VALUES (171, 'content provider');
INSERT INTO public.skills (id, name) VALUES (172, 'broadcast receiver');
INSERT INTO public.skills (id, name) VALUES (173, 'interface');
INSERT INTO public.skills (id, name) VALUES (174, 'jetpack compose');
INSERT INTO public.skills (id, name) VALUES (175, 'layout');
INSERT INTO public.skills (id, name) VALUES (176, 'элементы');
INSERT INTO public.skills (id, name) VALUES (177, 'frame');
INSERT INTO public.skills (id, name) VALUES (178, 'linear');
INSERT INTO public.skills (id, name) VALUES (179, 'relative');
INSERT INTO public.skills (id, name) VALUES (180, 'constraint');
INSERT INTO public.skills (id, name) VALUES (181, 'recycleview');
INSERT INTO public.skills (id, name) VALUES (182, 'textview');
INSERT INTO public.skills (id, name) VALUES (183, 'toast');
INSERT INTO public.skills (id, name) VALUES (184, 'dialog');
INSERT INTO public.skills (id, name) VALUES (185, 'button');
INSERT INTO public.skills (id, name) VALUES (186, 'bottom sheet');
INSERT INTO public.skills (id, name) VALUES (187, 'imageview');
INSERT INTO public.skills (id, name) VALUES (188, 'tab');
INSERT INTO public.skills (id, name) VALUES (189, 'edittext');
INSERT INTO public.skills (id, name) VALUES (190, 'drawer');
INSERT INTO public.skills (id, name) VALUES (191, 'listview');
INSERT INTO public.skills (id, name) VALUES (192, 'animations');
INSERT INTO public.skills (id, name) VALUES (193, 'mvi');
INSERT INTO public.skills (id, name) VALUES (194, 'mvvm');
INSERT INTO public.skills (id, name) VALUES (195, 'mvp');
INSERT INTO public.skills (id, name) VALUES (196, 'mvc');
INSERT INTO public.skills (id, name) VALUES (197, 'flow');
INSERT INTO public.skills (id, name) VALUES (198, 'rxkotlin');
INSERT INTO public.skills (id, name) VALUES (199, 'rxjava');
INSERT INTO public.skills (id, name) VALUES (200, 'livedata');
INSERT INTO public.skills (id, name) VALUES (201, 'работа с зависимостями');
INSERT INTO public.skills (id, name) VALUES (202, 'dagger');
INSERT INTO public.skills (id, name) VALUES (203, 'hilt');
INSERT INTO public.skills (id, name) VALUES (204, 'koin');
INSERT INTO public.skills (id, name) VALUES (205, 'kodein');
INSERT INTO public.skills (id, name) VALUES (206, 'наблюдатель');
INSERT INTO public.skills (id, name) VALUES (207, 'локальное хранение');
INSERT INTO public.skills (id, name) VALUES (208, 'shared preferences');
INSERT INTO public.skills (id, name) VALUES (209, 'encrypted shared preferences');
INSERT INTO public.skills (id, name) VALUES (210, 'datastore');
INSERT INTO public.skills (id, name) VALUES (211, 'room database');
INSERT INTO public.skills (id, name) VALUES (212, 'file system');
INSERT INTO public.skills (id, name) VALUES (213, 'retrofit');
INSERT INTO public.skills (id, name) VALUES (214, 'okhttp');
INSERT INTO public.skills (id, name) VALUES (215, 'coroutines');
INSERT INTO public.skills (id, name) VALUES (216, 'threads');
INSERT INTO public.skills (id, name) VALUES (217, 'workmanager');
INSERT INTO public.skills (id, name) VALUES (218, 'ktlint');
INSERT INTO public.skills (id, name) VALUES (219, 'detekt');
INSERT INTO public.skills (id, name) VALUES (220, 'espresso');
INSERT INTO public.skills (id, name) VALUES (221, 'junit');
INSERT INTO public.skills (id, name) VALUES (222, 'gradle');
INSERT INTO public.skills (id, name) VALUES (223, 'maven');
INSERT INTO public.skills (id, name) VALUES (224, 'gradle kotlin dsl');
INSERT INTO public.skills (id, name) VALUES (225, 'build.gradle.kts');
INSERT INTO public.skills (id, name) VALUES (226, 'settings.gradle.kts');

INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (1, 7, 53, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (2, 7, 54, 1, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (3, 7, 55, 1, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (4, 7, 56, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (5, 7, 5, 4, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (6, 7, 8, 4, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (7, 7, 41, 4, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (8, 7, 44, 4, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (9, 7, 57, 4, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (10, 7, 58, 4, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (11, 7, 59, 4, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (12, 7, 60, 4, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (13, 7, 61, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (14, 7, 10, 13, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (15, 7, 20, 13, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (16, 7, 62, 13, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (17, 7, 95, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (18, 7, 63, 17, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (19, 7, 64, 17, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (20, 7, 43, 17, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (21, 7, 39, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (22, 7, 65, 21, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (23, 7, 66, 21, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (24, 7, 67, 21, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (25, 7, 68, 21, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (26, 7, 69, 21, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (27, 7, 70, 21, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (28, 7, 71, 21, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (29, 7, 72, 21, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (30, 7, 73, 21, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (31, 7, 75, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (32, 7, 74, 31, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (33, 7, 48, 31, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (34, 7, 76, 31, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (35, 7, 77, 31, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (36, 7, 78, NULL, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (37, 7, 79, 36, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (38, 7, 80, 36, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (39, 7, 81, 36, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (40, 7, 101, 36, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (41, 7, 102, 36, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (42, 7, 103, 36, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (43, 7, 104, 36, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (44, 7, 82, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (45, 7, 83, 44, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (46, 7, 84, 44, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (47, 7, 85, 44, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (48, 7, 86, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (49, 7, 87, 48, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (50, 7, 88, 48, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (51, 7, 133, NULL, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (52, 7, 89, 51, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (53, 7, 90, 51, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (54, 7, 91, 51, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (55, 7, 92, 51, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (56, 7, 93, 51, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (57, 7, 94, 51, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (58, 7, 96, 51, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (59, 7, 100, NULL, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (60, 7, 97, 59, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (61, 7, 98, 59, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (62, 7, 99, 59, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (63, 7, 134, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (64, 7, 49, 63, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (65, 7, 50, 63, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (66, 7, 51, 63, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (67, 7, 105, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (68, 7, 106, 67, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (69, 7, 107, 67, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (70, 7, 108, 67, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (71, 7, 109, 67, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (72, 7, 110, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (73, 7, 111, 72, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (74, 7, 112, 72, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (75, 7, 47, 72, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (76, 7, 131, NULL, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (77, 7, 113, 76, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (78, 7, 114, 76, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (79, 7, 115, 76, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (80, 7, 116, 76, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (81, 7, 117, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (82, 7, 118, 81, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (83, 7, 119, 81, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (84, 7, 120, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (85, 7, 121, 84, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (86, 7, 122, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (87, 7, 123, 86, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (88, 7, 124, 86, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (89, 7, 125, 86, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (90, 7, 48, 86, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (91, 7, 135, NULL, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (92, 7, 126, 91, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (93, 7, 127, 91, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (94, 7, 128, 91, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (95, 7, 129, 91, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (96, 7, 130, 91, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (97, 7, 132, 91, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (98, 9, 53, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (99, 9, 54, 98, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (100, 9, 55, 98, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (101, 9, 56, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (102, 9, 5, 101, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (103, 9, 8, 101, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (104, 9, 23, 101, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (105, 9, 38, 101, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (106, 9, 136, 103, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (107, 9, 61, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (108, 9, 10, 107, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (109, 9, 20, 107, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (110, 9, 62, 107, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (111, 9, 137, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (112, 9, 138, 111, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (113, 9, 139, 111, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (114, 9, 140, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (115, 9, 25, 114, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (116, 9, 3, 114, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (117, 9, 7, 114, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (118, 9, 141, 114, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (119, 9, 142, 114, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (120, 9, 21, 105, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (121, 9, 26, 105, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (122, 9, 15, 103, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (123, 9, 16, 103, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (124, 9, 24, 103, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (125, 9, 30, 103, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (126, 9, 143, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (127, 9, 149, 126, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (128, 9, 144, 127, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (129, 9, 145, 127, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (130, 9, 146, 126, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (131, 9, 147, 130, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (132, 9, 148, 130, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (133, 9, 33, 130, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (134, 9, 82, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (135, 9, 150, 134, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (136, 9, 151, 134, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (137, 9, 152, 134, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (138, 9, 153, 134, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (139, 9, 39, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (140, 9, 65, 139, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (141, 9, 66, 139, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (142, 9, 67, 139, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (143, 9, 68, 139, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (144, 9, 69, 139, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (145, 9, 70, 139, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (146, 9, 71, 139, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (147, 9, 72, 139, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (148, 9, 73, 139, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (149, 9, 78, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (150, 9, 79, 149, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (151, 9, 80, 149, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (152, 9, 81, 149, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (153, 9, 101, 149, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (154, 9, 102, 149, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (155, 9, 103, 149, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (156, 9, 104, 149, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (157, 9, 154, NULL, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (158, 9, 155, 114, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (159, 5, 56, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (160, 5, 156, 159, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (161, 5, 59, 159, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (162, 5, 159, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (163, 5, 157, 162, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (164, 5, 158, 162, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (165, 5, 12, 162, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (166, 5, 61, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (167, 5, 10, 166, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (168, 5, 20, 166, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (169, 5, 62, 166, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (170, 5, 160, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (171, 5, 161, 170, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (172, 5, 162, 171, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (173, 5, 163, 171, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (174, 5, 164, 171, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (175, 5, 165, 170, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (176, 5, 166, 170, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (177, 5, 167, 176, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (178, 5, 168, 176, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (179, 5, 169, 176, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (180, 5, 170, 170, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (181, 5, 171, 170, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (182, 5, 172, 170, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (183, 5, 173, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (184, 5, 174, 183, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (185, 5, 73, 183, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (186, 5, 175, 183, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (187, 5, 176, 183, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (188, 5, 177, 186, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (189, 5, 178, 186, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (190, 5, 179, 186, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (191, 5, 180, 186, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (192, 5, 181, 186, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (193, 5, 182, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (194, 5, 183, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (195, 5, 184, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (196, 5, 185, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (197, 5, 186, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (198, 5, 187, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (199, 5, 188, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (200, 5, 189, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (201, 5, 190, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (202, 5, 191, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (203, 5, 192, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (204, 5, 165, 187, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (205, 5, 105, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (206, 5, 193, 205, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (207, 5, 194, 205, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (208, 5, 195, 205, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (209, 5, 196, 205, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (210, 5, 157, 205, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (211, 5, 206, 210, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (212, 5, 197, 211, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (213, 5, 198, 211, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (214, 5, 199, 211, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (215, 5, 200, 211, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (216, 5, 201, 205, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (217, 5, 202, 216, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (218, 5, 203, 216, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (219, 5, 204, 216, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (220, 5, 205, 216, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (221, 5, 207, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (222, 5, 208, 221, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (223, 5, 209, 221, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (224, 5, 210, 221, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (225, 5, 211, 221, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (226, 5, 212, 221, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (227, 5, 53, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (228, 5, 213, 227, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (229, 5, 214, 227, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (230, 5, 215, 227, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (231, 5, 216, 227, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (232, 5, 198, 227, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (233, 5, 199, 227, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (234, 5, 217, 227, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (235, 5, 125, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (236, 5, 149, NULL, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (237, 5, 218, 236, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (238, 5, 219, 236, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (239, 5, 82, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (240, 5, 220, 239, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (241, 5, 221, 239, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (242, 5, 143, NULL, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (243, 5, 222, 242, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (244, 5, 223, 242, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (245, 5, 224, 243, true);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (246, 5, 225, 243, false);
INSERT INTO public.roadmap_nodes (id, roadmap_id, skill_id, parent_id, is_optional) VALUES (247, 5, 226, 243, false);

--
-- Name: roadmap_nodes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roadmap_nodes_id_seq', 247, true);


--
-- Name: roadmaps_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roadmaps_id_seq', 24, true);


--
-- Name: skills_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.skills_id_seq', 226, true);
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
DELETE FROM public.roadmap_nodes WHERE id BETWEEN 0 AND 248;

DELETE FROM public.roadmaps WHERE id BETWEEN 0 AND 25;

DELETE FROM public.skills WHERE id BETWEEN 2 AND 227;

SELECT pg_catalog.setval('public.roadmap_nodes_id_seq', 1, true);

SELECT pg_catalog.setval('public.roadmaps_id_seq', 1, true);

SELECT pg_catalog.setval('public.skills_id_seq', 1, true);
""")
