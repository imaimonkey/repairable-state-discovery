# V2R cluster inventory

2026-09-26T01:09:25.254122+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318658969600 available bytes; 82.22% used; 112476292 free inodes.

server1 `/home`: 318658969600 available bytes; 82.22% used; 112476292 free inodes.

server1 `/tmp`: 318658969600 available bytes; 82.22% used; 112476292 free inodes.

server1 `/var/tmp`: 318658969600 available bytes; 82.22% used; 112476292 free inodes.

server1 `/mnt/raid5`: 345546244096 available bytes; 98.41% used; 337546650 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940426240 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22940426240 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22940426240 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22940426240 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 293806931968 available bytes; 97.97% used; 445056601 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341141504 available bytes; 95.29% used; 114152424 free inodes.

server3 `/home`: 84341141504 available bytes; 95.29% used; 114152424 free inodes.

server3 `/data`: 124933689344 available bytes; 98.27% used; 225818373 free inodes.

server3 `/tmp`: 84341141504 available bytes; 95.29% used; 114152424 free inodes.

server3 `/var/tmp`: 84341141504 available bytes; 95.29% used; 114152424 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105281515520 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281515520 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141761032192 available bytes; 98.04% used; 224917327 free inodes.

server4 `/tmp`: 105281515520 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281515520 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
