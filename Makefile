CC = cc
CFLAGS = -Wall -Wextra -Werror
NAME = libftprintf.a

SRCS  = ft_check_format.c ft_printf.c ./utils/ft_putchar.c ./utils/ft_putnbr.c ./utils/ft_putstr.c ./utils/ft_puthex.c ./utils/ft_putnbr_unsigned.c ./utils/ft_strlen.c

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

clean:
	rm -rf $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean