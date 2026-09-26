# V2R cluster inventory

2026-09-26T06:08:40.256159+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318779777024 available bytes; 82.22% used; 112476280 free inodes.

server1 `/home`: 318779777024 available bytes; 82.22% used; 112476280 free inodes.

server1 `/tmp`: 318779777024 available bytes; 82.22% used; 112476280 free inodes.

server1 `/var/tmp`: 318779777024 available bytes; 82.22% used; 112476280 free inodes.

server1 `/mnt/raid5`: 223908032512 available bytes; 98.97% used; 337539919 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 20783558656 available bytes; 98.84% used; 110404634 free inodes.

server2 `/home`: 20783558656 available bytes; 98.84% used; 110404634 free inodes.

server2 `/tmp`: 20783558656 available bytes; 98.84% used; 110404634 free inodes.

server2 `/var/tmp`: 20783558656 available bytes; 98.84% used; 110404634 free inodes.

server2 `/mnt/raid5`: 274321137664 available bytes; 98.10% used; 445033356 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82430693376 available bytes; 95.40% used; 114110905 free inodes.

server3 `/home`: 82430693376 available bytes; 95.40% used; 114110905 free inodes.

server3 `/data`: 123994521600 available bytes; 98.29% used; 225822632 free inodes.

server3 `/tmp`: 82430693376 available bytes; 95.40% used; 114110905 free inodes.

server3 `/var/tmp`: 82430693376 available bytes; 95.40% used; 114110905 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106093772800 available bytes; 94.08% used; 114348193 free inodes.

server4 `/home`: 106093772800 available bytes; 94.08% used; 114348193 free inodes.

server4 `/data`: 106915364864 available bytes; 98.52% used; 224929110 free inodes.

server4 `/tmp`: 106093772800 available bytes; 94.08% used; 114348193 free inodes.

server4 `/var/tmp`: 106093772800 available bytes; 94.08% used; 114348193 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
