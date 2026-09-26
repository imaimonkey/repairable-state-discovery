# V2R cluster inventory

2026-09-26T08:02:42.570695+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318750916608 available bytes; 82.22% used; 112476271 free inodes.

server1 `/home`: 318750916608 available bytes; 82.22% used; 112476271 free inodes.

server1 `/tmp`: 318750916608 available bytes; 82.22% used; 112476271 free inodes.

server1 `/var/tmp`: 318750916608 available bytes; 82.22% used; 112476271 free inodes.

server1 `/mnt/raid5`: 219165446144 available bytes; 98.99% used; 337539081 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22321061888 available bytes; 98.75% used; 110403907 free inodes.

server2 `/home`: 22321061888 available bytes; 98.75% used; 110403907 free inodes.

server2 `/tmp`: 22321061888 available bytes; 98.75% used; 110403907 free inodes.

server2 `/var/tmp`: 22321061888 available bytes; 98.75% used; 110403907 free inodes.

server2 `/mnt/raid5`: 256520777728 available bytes; 98.23% used; 445025741 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82678554624 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82678554624 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123889786880 available bytes; 98.29% used; 225820493 free inodes.

server3 `/tmp`: 82678554624 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82678554624 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106073419776 available bytes; 94.08% used; 114348153 free inodes.

server4 `/home`: 106073419776 available bytes; 94.08% used; 114348153 free inodes.

server4 `/data`: 105374887936 available bytes; 98.54% used; 224922241 free inodes.

server4 `/tmp`: 106073419776 available bytes; 94.08% used; 114348153 free inodes.

server4 `/var/tmp`: 106073419776 available bytes; 94.08% used; 114348153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
