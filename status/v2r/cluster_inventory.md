# V2R cluster inventory

2026-09-26T06:13:15.001730+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318779129856 available bytes; 82.22% used; 112476277 free inodes.

server1 `/home`: 318779129856 available bytes; 82.22% used; 112476277 free inodes.

server1 `/tmp`: 318779129856 available bytes; 82.22% used; 112476277 free inodes.

server1 `/var/tmp`: 318779129856 available bytes; 82.22% used; 112476277 free inodes.

server1 `/mnt/raid5`: 220861648896 available bytes; 98.99% used; 337539887 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19690475520 available bytes; 98.90% used; 110401408 free inodes.

server2 `/home`: 19690475520 available bytes; 98.90% used; 110401408 free inodes.

server2 `/tmp`: 19690475520 available bytes; 98.90% used; 110401408 free inodes.

server2 `/var/tmp`: 19690475520 available bytes; 98.90% used; 110401408 free inodes.

server2 `/mnt/raid5`: 272995594240 available bytes; 98.11% used; 445029401 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82565234688 available bytes; 95.39% used; 114110907 free inodes.

server3 `/home`: 82565234688 available bytes; 95.39% used; 114110907 free inodes.

server3 `/data`: 123992252416 available bytes; 98.29% used; 225822567 free inodes.

server3 `/tmp`: 82565234688 available bytes; 95.39% used; 114110907 free inodes.

server3 `/var/tmp`: 82565234688 available bytes; 95.39% used; 114110907 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105990201344 available bytes; 94.09% used; 114347063 free inodes.

server4 `/home`: 105990201344 available bytes; 94.09% used; 114347063 free inodes.

server4 `/data`: 106644742144 available bytes; 98.53% used; 224923660 free inodes.

server4 `/tmp`: 105990201344 available bytes; 94.09% used; 114347063 free inodes.

server4 `/var/tmp`: 105990201344 available bytes; 94.09% used; 114347063 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
