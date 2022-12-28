co_ord_1 = (0, 0, 0)
co_ord_2 = (10, 5, 0)
co_ord_3 = (20, 0, 0)
co_ord_4 = (30, 5, 0)
co_ord_5 = (40, 0, 0)


def create_extrusion(
    part, hsf, hb, co_ord_1=co_ord_1, co_ord_2=co_ord_2, co_ord_3=co_ord_3, co_ord_4=co_ord_4, co_ord_5=co_ord_5
):
    """

    :param hb:
    :param part:
    :param hsf:
    :param co_ord_1:
    :param co_ord_2:
    :param co_ord_3:
    :param co_ord_4:
    :param co_ord_5:
    :return:
    """
    point_1 = hsf.add_new_point_coord(co_ord_1[0], co_ord_1[1], co_ord_1[2])
    point_2 = hsf.add_new_point_coord(co_ord_2[0], co_ord_2[1], co_ord_2[2])
    point_3 = hsf.add_new_point_coord(co_ord_3[0], co_ord_3[1], co_ord_3[2])
    point_4 = hsf.add_new_point_coord(co_ord_4[0], co_ord_4[1], co_ord_4[2])
    point_5 = hsf.add_new_point_coord(co_ord_5[0], co_ord_5[1], co_ord_5[2])

    hb.append_hybrid_shape(point_1)
    hb.append_hybrid_shape(point_2)
    hb.append_hybrid_shape(point_3)
    hb.append_hybrid_shape(point_4)
    hb.append_hybrid_shape(point_5)

    spline = hsf.add_new_spline()
    spline.add_point(point_1)
    spline.add_point(point_2)
    spline.add_point(point_3)
    spline.add_point(point_4)
    spline.add_point(point_5)

    hb.append_hybrid_shape(spline)

    plane = part.origin_elements.plane_xy

    direction = hsf.add_new_direction(plane)
    extrusion = hsf.add_new_extrude(spline, i_offset_debut=10, i_offset_fin=10, i_direction=direction)
    hb.append_hybrid_shape(extrusion)

    return extrusion
