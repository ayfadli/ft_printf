/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ayfadli <ayfadli@student.1337.ma>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 17:55:31 by ayfadli           #+#    #+#             */
/*   Updated: 2025/11/17 17:57:03 by ayfadli          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef UTILS_H
# define UTILS_H
# include <unistd.h>

int		ft_putchar(char c);
int		ft_putnbr(int n);
int		ft_putnbr_unsigned(unsigned int n);
int		ft_putstr(const char *s);
int		ft_puthex(unsigned	long n, const char format);
size_t	ft_strlen(const char *s);

#endif