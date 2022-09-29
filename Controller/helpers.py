def draw_text(text, font, colour, screen, pos, alignment):
    text_obj = font.render(text, 1, colour)
    text_rect = text_obj.get_rect()
    if alignment == 'center':
        text_rect.center = (pos)
    if alignment == 'right':
        text_rect.topright = (pos)
    if alignment == 'left':
        text_rect.topleft = (pos)
    screen.blit(text_obj, text_rect)
