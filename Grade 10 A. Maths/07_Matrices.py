from manim import *

class ConicSectionMorph(ThreeDScene):
    def construct(self):
        a = 1
        tracker = ValueTracker(-1.5)  # controls plane slope k

        cone = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                a * u,
            ]),
            u_range=[0, 2],
            v_range=[0, TAU],
            resolution=(24, 64),
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.4,
        )
        self.add(cone)

        def param_curve(t):
            k = tracker.get_value()
            # Intersection with plane: z = k*y + a
            # Using cone: x^2 + y^2 = (1/a) z^2  --> relate x,y,z
            # Solve for y(t), x(t), z(t) parametrically for given k
            # Example parameter t will vary along curve, tweak as needed

            # Sample parametric solution for demonstration:
            y = t
            z = k * y + a
            x = np.sqrt((1/a) * z**2 - y**2) if (1/a)*z**2 - y**2 >= 0 else 0
            return np.array([x, y, z])

        curve = always_redraw(
            lambda: ParametricFunction(
                param_curve,
                t_range=[-2, 2],
                color=YELLOW,
                stroke_width=4,
            )
        )

        self.add(curve)

        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.play(tracker.animate.set_value(1.5), run_time=8)
        self.wait()