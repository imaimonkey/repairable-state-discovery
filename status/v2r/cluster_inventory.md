# V2R cluster inventory

2026-09-26T09:19:26.310616+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318735978496 available bytes; 82.22% used; 112475775 free inodes.

server1 `/home`: 318735978496 available bytes; 82.22% used; 112475775 free inodes.

server1 `/tmp`: 318735978496 available bytes; 82.22% used; 112475775 free inodes.

server1 `/var/tmp`: 318735978496 available bytes; 82.22% used; 112475775 free inodes.

server1 `/mnt/raid5`: 198347603968 available bytes; 99.09% used; 337538700 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22324527104 available bytes; 98.75% used; 110403915 free inodes.

server2 `/home`: 22324527104 available bytes; 98.75% used; 110403915 free inodes.

server2 `/tmp`: 22324527104 available bytes; 98.75% used; 110403915 free inodes.

server2 `/var/tmp`: 22324527104 available bytes; 98.75% used; 110403915 free inodes.

server2 `/mnt/raid5`: 254519742464 available bytes; 98.24% used; 445023393 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82660687872 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82660687872 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 123660152832 available bytes; 98.29% used; 225828005 free inodes.

server3 `/tmp`: 82660687872 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82660687872 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106045882368 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106045882368 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89324875776 available bytes; 98.77% used; 224883313 free inodes.

server4 `/tmp`: 106045882368 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106045882368 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
