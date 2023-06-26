import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { formatXAxis } from "../../utils/charts";

export interface RequestChartDataPoint {
  success: number;
  error: number;
  timestamp: number;
}

export default function RequestChart({
  data,
}: {
  data: RequestChartDataPoint[];
}) {
  return (
    <ResponsiveContainer width="100%" height={500}>
      <AreaChart data={data} margin={{ right: 50, left: 30, top: 5 }}>
        <CartesianGrid
          strokeDasharray="4 3"
          strokeWidth={1}
          strokeOpacity={0.8}
          horizontal={true}
          vertical={false}
        />
        <Area type="monotone" dataKey="success" stroke="#000" fill="#000" />
        <Area type="monotone" dataKey="error" stroke="#f00" fill="#f00" />
        <XAxis
          dataKey="timestamp"
          axisLine={false}
          padding={{ left: 0 }}
          minTickGap={10}
          tickFormatter={formatXAxis}
          angle={-45}
          textAnchor="end"
          height={105}
        />
        <YAxis padding={{ top: 0 }} allowDecimals={false} />
        <Tooltip
          labelFormatter={(value) => formatXAxis(value)}
          formatter={(value, key) => {
            return [
              value as number,
              key === "error" ? "Failed requests" : "Successful Requests",
            ];
          }}
          cursor={{ fill: "#808080", fillOpacity: 0.3 }}
        />
      </AreaChart>
    </ResponsiveContainer>
  );
}
