-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Апр 08 2018 г., 09:21
-- Версия сервера: 10.1.21-MariaDB
-- Версия PHP: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `polls`
--

-- --------------------------------------------------------

--
-- Структура таблицы `polls`
--

CREATE TABLE `polls` (
  `id` int(11) NOT NULL,
  `poll_id` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `polls`
--

INSERT INTO `polls` (`id`, `poll_id`, `name`) VALUES
(1, 1, 'Юрфак');

-- --------------------------------------------------------

--
-- Структура таблицы `poll_options`
--

CREATE TABLE `poll_options` (
  `id` int(11) NOT NULL,
  `poll_id` int(11) NOT NULL,
  `title` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `poll_options`
--

INSERT INTO `poll_options` (`id`, `poll_id`, `title`) VALUES
(1, 1, 'Стасюк Дарья'),
(2, 1, 'Гирш Мария'),
(3, 1, 'Бобровая София'),
(4, 1, 'Гордеева Жанна'),
(5, 1, 'Сергеева Юлия'),
(6, 1, 'Семенцова Юта'),
(7, 1, 'Худеньких Алина'),
(8, 1, 'Захарова Олеся'),
(9, 1, 'Набокова Дарья'),
(10, 1, 'Морошкина Олеся'),
(11, 1, 'Чернопиская Наталья'),
(12, 1, 'Черняк Мария');

-- --------------------------------------------------------

--
-- Структура таблицы `poll_votes`
--

CREATE TABLE `poll_votes` (
  `id` int(11) NOT NULL,
  `poll_id` int(11) NOT NULL,
  `option_id` int(11) NOT NULL,
  `number` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `poll_votes`
--

INSERT INTO `poll_votes` (`id`, `poll_id`, `option_id`, `number`) VALUES
(1, 1, 1, '89526453656'),
(2, 1, 1, '239453045');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `polls`
--
ALTER TABLE `polls`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `poll_options`
--
ALTER TABLE `poll_options`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Индексы таблицы `poll_votes`
--
ALTER TABLE `poll_votes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `id_2` (`id`),
  ADD KEY `id_3` (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `polls`
--
ALTER TABLE `polls`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT для таблицы `poll_options`
--
ALTER TABLE `poll_options`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT для таблицы `poll_votes`
--
ALTER TABLE `poll_votes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
