/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_check_format.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ayfadli <ayfadli@student.1337.ma>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 10:50:16 by ayfadli           #+#    #+#             */
/*   Updated: 2025/11/22 20:55:39 by ayfadli          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_check_format(const char format, va_list args)
{
	void	*ptr;

	if (format == '%')
		return (ft_putchar(format));
	else if (format == 'd' || format == 'i')
		return (ft_putnbr(va_arg(args, int)));
	else if (format == 'c')
		return (ft_putchar(va_arg(args, int)));
	else if ((format == 's'))
		return (ft_putstr(va_arg(args, char *)));
	else if (format == 'p')
	{
		ptr = va_arg(args, void *);
		if (ptr)
			return (ft_puthex((unsigned long)ptr, format));
		return (ft_putstr("(nil)"));
	}
	else if (format == 'u')
		return (ft_putnbr_unsigned(va_arg(args, unsigned int)));
	else if (format == 'x' || format == 'X')
		return (ft_puthex((unsigned long)va_arg(args, unsigned int), format));
	return (0);
}
