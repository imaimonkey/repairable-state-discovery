# V2R cluster inventory

2026-09-24T22:19:12.191749+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323947376640 available bytes; 81.93% used; 112481416 free inodes.

server1 `/home`: 323947376640 available bytes; 81.93% used; 112481416 free inodes.

server1 `/tmp`: 323947376640 available bytes; 81.93% used; 112481416 free inodes.

server1 `/var/tmp`: 323947376640 available bytes; 81.93% used; 112481416 free inodes.

server1 `/mnt/raid5`: 415397625856 available bytes; 98.09% used; 337621605 free inodes.
| server2 | True | [] | [] |

server2 `/`: 29081190400 available bytes; 98.38% used; 110411244 free inodes.

server2 `/home`: 29081190400 available bytes; 98.38% used; 110411244 free inodes.

server2 `/tmp`: 29081190400 available bytes; 98.38% used; 110411244 free inodes.

server2 `/var/tmp`: 29081190400 available bytes; 98.38% used; 110411244 free inodes.

server2 `/mnt/raid5`: 488878329856 available bytes; 96.62% used; 445153367 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84377817088 available bytes; 95.29% used; 114156087 free inodes.

server3 `/home`: 84377817088 available bytes; 95.29% used; 114156087 free inodes.

server3 `/data`: 149456306176 available bytes; 97.93% used; 225802275 free inodes.

server3 `/tmp`: 84377817088 available bytes; 95.29% used; 114156087 free inodes.

server3 `/var/tmp`: 84377817088 available bytes; 95.29% used; 114156087 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810640896 available bytes; 94.10% used; 114348325 free inodes.

server4 `/home`: 105810640896 available bytes; 94.10% used; 114348325 free inodes.

server4 `/data`: 73372205056 available bytes; 98.99% used; 225231465 free inodes.

server4 `/tmp`: 105810640896 available bytes; 94.10% used; 114348325 free inodes.

server4 `/var/tmp`: 105810640896 available bytes; 94.10% used; 114348325 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
