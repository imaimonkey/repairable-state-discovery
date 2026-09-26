# V2R cluster inventory

2026-09-26T09:24:00.923374+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318636978176 available bytes; 82.22% used; 112475123 free inodes.

server1 `/home`: 318636978176 available bytes; 82.22% used; 112475123 free inodes.

server1 `/tmp`: 318636978176 available bytes; 82.22% used; 112475123 free inodes.

server1 `/var/tmp`: 318636978176 available bytes; 82.22% used; 112475123 free inodes.

server1 `/mnt/raid5`: 218984579072 available bytes; 99.00% used; 337538689 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22322941952 available bytes; 98.75% used; 110403919 free inodes.

server2 `/home`: 22322941952 available bytes; 98.75% used; 110403919 free inodes.

server2 `/tmp`: 22322941952 available bytes; 98.75% used; 110403919 free inodes.

server2 `/var/tmp`: 22322941952 available bytes; 98.75% used; 110403919 free inodes.

server2 `/mnt/raid5`: 254381170688 available bytes; 98.24% used; 445023071 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82663530496 available bytes; 95.39% used; 114110811 free inodes.

server3 `/home`: 82663530496 available bytes; 95.39% used; 114110811 free inodes.

server3 `/data`: 123659829248 available bytes; 98.29% used; 225827941 free inodes.

server3 `/tmp`: 82663530496 available bytes; 95.39% used; 114110811 free inodes.

server3 `/var/tmp`: 82663530496 available bytes; 95.39% used; 114110811 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106045722624 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106045722624 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89324683264 available bytes; 98.77% used; 224883314 free inodes.

server4 `/tmp`: 106045722624 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106045722624 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
