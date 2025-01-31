from __future__ import annotations

from test_prettytable import helper_table

from prettytable import PrettyTable, TableStyle


class TestRowEndSection:
    def test_row_end_section(self) -> None:
        table = PrettyTable()
        table.set_style(TableStyle.SINGLE_BORDER)
        v = 1
        for row in range(4):
            if row % 2 == 0:
                table.add_row(
                    [f"value {v}", f"value{v+1}", f"value{v+2}"], divider=True
                )
            else:
                table.add_row(
                    [f"value {v}", f"value{v+1}", f"value{v+2}"], divider=False
                )
            v += 3
        table.del_row(0)
        print(table)
        assert (
            table.get_string().strip()
            == """
┌──────────┬─────────┬─────────┐
│ Field 1  │ Field 2 │ Field 3 │
├──────────┼─────────┼─────────┤
│ value 4  │  value5 │  value6 │
│ value 7  │  value8 │  value9 │
├──────────┼─────────┼─────────┤
│ value 10 │ value11 │ value12 │
└──────────┴─────────┴─────────┘
""".strip()
        )


class TestClearing:
    def test_clear_rows(self) -> None:
        t = helper_table()
        t.add_row([0, "a", "b", "c"], divider=True)
        t.clear_rows()
        assert t.rows == []
        assert t.dividers == []
        assert t.field_names == ["", "Field 1", "Field 2", "Field 3"]

    def test_clear(self) -> None:
        t = helper_table()
        t.add_row([0, "a", "b", "c"], divider=True)
        t.clear()
        assert t.rows == []
        assert t.dividers == []
        assert t.field_names == []
