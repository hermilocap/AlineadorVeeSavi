-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 09-07-2018 a las 02:20:37
-- Versión del servidor: 5.5.24-log
-- Versión de PHP: 5.4.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `bdveesavi`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alineados`
--

CREATE TABLE IF NOT EXISTS `alineados` (
  `idalineacion` int(11) DEFAULT NULL,
  `oracionespaniol` text,
  `oracionmixteco` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `alineados`
--

INSERT INTO `alineados` (`idalineacion`, `oracionespaniol`, `oracionmixteco`) VALUES
(1, '﻿10 derechos generales de los pacientes', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.'),
(2, 'Recibir atención médica adecuada.', 'Iyo cha cuiti chihin cun cha cua ndehe vaha iin dotor chihin cun cuhva cha tahan chi.'),
(3, 'Recibir trato digno y respetuoso.', 'Iyo cha cuiti chihin cun cha cua tayahvi ra dotor ndihi cha cuiti cha iyo chihun, ta cua sacahnu ra chihun.'),
(4, 'Recibir información suficiente, clara, oportuna y veraz.', 'Iyo cha cuiti chihin cun cha cua cati tuhun vaha ra dotor chihun hora cha tahan chi, ta cua cati ra cha ndicha chihin cun.'),
(5, 'Decidir libremente sobre tu atención.', 'Iyo cha cuiti chihin cun cha cua cati maun yoso cuhva cua ndehe ra dotor chihun.'),
(6, 'Otorgar o no tu consentimiento válidamente informado.', 'Iyo cha cuiti chihin cun cha cua cati tuhun vaha ñi chihin cun, ta cua cati maan cun ndaa cha cuni cun a ña cuni cun.'),
(7, 'Ser tratado con confidencialidad.', 'Iyo cha cuiti chihin cun tu cuni cun cha yoni cua coto ñaan tahan cun.'),
(8, 'Contar con facilidades para obtener una segunda opinión.', 'Iyo cha cuiti chihin cun cha cua cuhun cun nuun inca dotor, ta cua nducu tuhun cun ñaan tahan cun.'),
(9, 'Recibir atención médica en caso de urgencia.', 'Iyo cha cuiti chihin cun cha quii ni cua ndehe dotor chihin cun tu cha iyo xaan tahan cun cha cuhvi cun.'),
(10, 'Contar con un expediente clínico.', 'Iyo cha cuiti chihin cun cha cua coo iin tutu cuenda ndihi cuehe cha tahan cun.'),
(11, 'Ser atendido cuando te inconformes por la atención médica recibida.', 'Iyo cha cuiti chihin cun cha cua cahan ñivi cha cahun tu cua xico tuhun cun chi iin dotor cha ña ndehe vaha chihin cun.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `corpusespaniol`
--

CREATE TABLE IF NOT EXISTS `corpusespaniol` (
  `idcorpusespaniol` int(11) DEFAULT NULL,
  `oracioncorpusespaniol` text,
  `titulocorpusespaniol` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `corpusespaniol`
--

INSERT INTO `corpusespaniol` (`idcorpusespaniol`, `oracioncorpusespaniol`, `titulocorpusespaniol`) VALUES
(1, '﻿10 derechos generales de los pacientes', '﻿10 derechos generales de los pacientes\n'),
(2, 'Recibir atención médica adecuada.', '﻿10 derechos generales de los pacientes\n'),
(3, 'Recibir trato digno y respetuoso.', '﻿10 derechos generales de los pacientes\n'),
(4, 'Recibir información suficiente, clara, oportuna y veraz.', '﻿10 derechos generales de los pacientes\n'),
(5, 'Decidir libremente sobre tu atención.', '﻿10 derechos generales de los pacientes\n'),
(6, 'Otorgar o no tu consentimiento válidamente informado.', '﻿10 derechos generales de los pacientes\n'),
(7, 'Ser tratado con confidencialidad.', '﻿10 derechos generales de los pacientes\n'),
(8, 'Contar con facilidades para obtener una segunda opinión.', '﻿10 derechos generales de los pacientes\n'),
(9, 'Recibir atención médica en caso de urgencia.', '﻿10 derechos generales de los pacientes\n'),
(10, 'Contar con un expediente clínico.', '﻿10 derechos generales de los pacientes\n'),
(11, 'Ser atendido cuando te inconformes por la atención médica recibida.', '﻿10 derechos generales de los pacientes\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `corpusmixteco`
--

CREATE TABLE IF NOT EXISTS `corpusmixteco` (
  `idcorpusmixteco` int(11) DEFAULT NULL,
  `oracioncorpusmixteco` text,
  `titulocorpusmixteco` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `corpusmixteco`
--

INSERT INTO `corpusmixteco` (`idcorpusmixteco`, `oracioncorpusmixteco`, `titulocorpusmixteco`) VALUES
(1, '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(2, 'Iyo cha cuiti chihin cun cha cua ndehe vaha iin dotor chihin cun cuhva cha tahan chi.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(3, 'Iyo cha cuiti chihin cun cha cua tayahvi ra dotor ndihi cha cuiti cha iyo chihun, ta cua sacahnu ra chihun.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(4, 'Iyo cha cuiti chihin cun cha cua cati tuhun vaha ra dotor chihun hora cha tahan chi, ta cua cati ra cha ndicha chihin cun.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(5, 'Iyo cha cuiti chihin cun cha cua cati maun yoso cuhva cua ndehe ra dotor chihun.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(6, 'Iyo cha cuiti chihin cun cha cua cati tuhun vaha ñi chihin cun, ta cua cati maan cun ndaa cha cuni cun a ña cuni cun.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(7, 'Iyo cha cuiti chihin cun tu cuni cun cha yoni cua coto ñaan tahan cun.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(8, 'Iyo cha cuiti chihin cun cha cua cuhun cun nuun inca dotor, ta cua nducu tuhun cun ñaan tahan cun.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(9, 'Iyo cha cuiti chihin cun cha quii ni cua ndehe dotor chihin cun tu cha iyo xaan tahan cun cha cuhvi cun.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(10, 'Iyo cha cuiti chihin cun cha cua coo iin tutu cuenda ndihi cuehe cha tahan cun.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n'),
(11, 'Iyo cha cuiti chihin cun cha cua cahan ñivi cha cahun tu cua xico tuhun cun chi iin dotor cha ña ndehe vaha chihin cun.', '﻿Uchi tahan cha cuiti iyo chi ñivi cuhvi.\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prealineados`
--

CREATE TABLE IF NOT EXISTS `prealineados` (
  `idprealineado` int(11) DEFAULT NULL,
  `preoracionespaniol` text,
  `preoracionmixteco` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
