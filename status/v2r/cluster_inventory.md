# V2R cluster inventory

2026-09-27T10:19:56.057291+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314440351744 available bytes; 82.46% used; 112440675 free inodes.

server1 `/home`: 314440351744 available bytes; 82.46% used; 112440675 free inodes.

server1 `/tmp`: 314440351744 available bytes; 82.46% used; 112440675 free inodes.

server1 `/var/tmp`: 314440351744 available bytes; 82.46% used; 112440675 free inodes.

server1 `/mnt/raid5`: 635421716480 available bytes; 97.09% used; 337424414 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16512241664 available bytes; 99.08% used; 110356612 free inodes.

server2 `/home`: 16512241664 available bytes; 99.08% used; 110356612 free inodes.

server2 `/tmp`: 16512241664 available bytes; 99.08% used; 110356612 free inodes.

server2 `/var/tmp`: 16512241664 available bytes; 99.08% used; 110356612 free inodes.

server2 `/mnt/raid5`: 572075225088 available bytes; 96.05% used; 444739330 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78544097280 available bytes; 95.62% used; 114062825 free inodes.

server3 `/home`: 78544097280 available bytes; 95.62% used; 114062825 free inodes.

server3 `/data`: 1332196626432 available bytes; 81.59% used; 225761095 free inodes.

server3 `/tmp`: 78544097280 available bytes; 95.62% used; 114062825 free inodes.

server3 `/var/tmp`: 78544097280 available bytes; 95.62% used; 114062825 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111040581632 available bytes; 93.80% used; 114372831 free inodes.

server4 `/home`: 111040581632 available bytes; 93.80% used; 114372831 free inodes.

server4 `/data`: 363693498368 available bytes; 94.97% used; 224766917 free inodes.

server4 `/tmp`: 111040581632 available bytes; 93.80% used; 114372831 free inodes.

server4 `/var/tmp`: 111040581632 available bytes; 93.80% used; 114372831 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
