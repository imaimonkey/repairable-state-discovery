# V2R cluster inventory

2026-09-24T07:04:42.923693+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324480712704 available bytes; 81.90% used; 112491334 free inodes.

server1 `/home`: 324480712704 available bytes; 81.90% used; 112491334 free inodes.

server1 `/tmp`: 324480712704 available bytes; 81.90% used; 112491334 free inodes.

server1 `/var/tmp`: 324480712704 available bytes; 81.90% used; 112491334 free inodes.

server1 `/mnt/raid5`: 517428912128 available bytes; 97.63% used; 337722837 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57861304320 available bytes; 96.77% used; 110431169 free inodes.

server2 `/home`: 57861304320 available bytes; 96.77% used; 110431169 free inodes.

server2 `/tmp`: 57861304320 available bytes; 96.77% used; 110431169 free inodes.

server2 `/var/tmp`: 57861304320 available bytes; 96.77% used; 110431169 free inodes.

server2 `/mnt/raid5`: 519165444096 available bytes; 96.41% used; 445190752 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127168016384 available bytes; 92.90% used; 114199241 free inodes.

server3 `/home`: 127168016384 available bytes; 92.90% used; 114199241 free inodes.

server3 `/data`: 139170385920 available bytes; 98.08% used; 225834675 free inodes.

server3 `/tmp`: 127168016384 available bytes; 92.90% used; 114199241 free inodes.

server3 `/var/tmp`: 127168016384 available bytes; 92.90% used; 114199241 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790246912 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105790246912 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 300574736384 available bytes; 95.85% used; 225367605 free inodes.

server4 `/tmp`: 105790246912 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105790246912 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
