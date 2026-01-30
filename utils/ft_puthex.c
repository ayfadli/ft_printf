/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ayfadli <ayfadli@student.1337.ma>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 10:50:49 by ayfadli           #+#    #+#             */
/*   Updated: 2025/11/17 17:52:39 by ayfadli          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "utils.h"

int	ft_puthex(unsigned	long n, char format)
{
	char	*hex;
	int		count;

	count = 0;
	if (format == 'x' || format == 'p')
		hex = "0123456789abcdef";
	else
		hex = "0123456789ABCDEF";
	if (format == 'p')
	{
		count += ft_putstr("0x");
		format = 'x';
	}
	if (n >= 16)
		count += ft_puthex(n / 16, format);
	count += ft_putchar(hex[n % 16]);
	return (count);
}
