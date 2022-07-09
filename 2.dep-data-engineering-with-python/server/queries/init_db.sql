CREATE TABLE IF NOT EXISTS `phone_book` (
  `id` int(5) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;



INSERT INTO `phone_book` (`id`, `name`, `phone`, `address`) VALUES
(16, 'Muhammad Hanif', '085733492411', 'Lamongan');


ALTER TABLE `phone_book`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `phone_book`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=21;