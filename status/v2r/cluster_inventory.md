# V2R cluster inventory

2026-09-26T08:39:46.600005+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318745698304 available bytes; 82.22% used; 112475802 free inodes.

server1 `/home`: 318745698304 available bytes; 82.22% used; 112475802 free inodes.

server1 `/tmp`: 318745698304 available bytes; 82.22% used; 112475802 free inodes.

server1 `/var/tmp`: 318745698304 available bytes; 82.22% used; 112475802 free inodes.

server1 `/mnt/raid5`: 219080028160 available bytes; 99.00% used; 337538893 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22319906816 available bytes; 98.75% used; 110403904 free inodes.

server2 `/home`: 22319906816 available bytes; 98.75% used; 110403904 free inodes.

server2 `/tmp`: 22319906816 available bytes; 98.75% used; 110403904 free inodes.

server2 `/var/tmp`: 22319906816 available bytes; 98.75% used; 110403904 free inodes.

server2 `/mnt/raid5`: 255419949056 available bytes; 98.24% used; 445024376 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82678935552 available bytes; 95.39% used; 114110813 free inodes.

server3 `/home`: 82678935552 available bytes; 95.39% used; 114110813 free inodes.

server3 `/data`: 123900432384 available bytes; 98.29% used; 225828644 free inodes.

server3 `/tmp`: 82678935552 available bytes; 95.39% used; 114110813 free inodes.

server3 `/var/tmp`: 82678935552 available bytes; 95.39% used; 114110813 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106063851520 available bytes; 94.08% used; 114348137 free inodes.

server4 `/home`: 106063851520 available bytes; 94.08% used; 114348137 free inodes.

server4 `/data`: 89364172800 available bytes; 98.76% used; 224883413 free inodes.

server4 `/tmp`: 106063851520 available bytes; 94.08% used; 114348137 free inodes.

server4 `/var/tmp`: 106063851520 available bytes; 94.08% used; 114348137 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
