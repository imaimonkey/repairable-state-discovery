# V2R cluster inventory

2026-09-24T00:23:13.110115+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325553750016 available bytes; 81.84% used; 112500665 free inodes.

server1 `/home`: 325553750016 available bytes; 81.84% used; 112500665 free inodes.

server1 `/tmp`: 325553750016 available bytes; 81.84% used; 112500665 free inodes.

server1 `/var/tmp`: 325553750016 available bytes; 81.84% used; 112500665 free inodes.

server1 `/mnt/raid5`: 1172465995776 available bytes; 94.62% used; 337735196 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41000468480 available bytes; 97.71% used; 110432363 free inodes.

server2 `/home`: 41000468480 available bytes; 97.71% used; 110432363 free inodes.

server2 `/tmp`: 41000468480 available bytes; 97.71% used; 110432363 free inodes.

server2 `/var/tmp`: 41000468480 available bytes; 97.71% used; 110432363 free inodes.

server2 `/mnt/raid5`: 533009178624 available bytes; 96.32% used; 445203650 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292637003776 available bytes; 83.67% used; 114209079 free inodes.

server3 `/home`: 292637003776 available bytes; 83.67% used; 114209079 free inodes.

server3 `/data`: 82246443008 available bytes; 98.86% used; 225844352 free inodes.

server3 `/tmp`: 292637003776 available bytes; 83.67% used; 114209079 free inodes.

server3 `/var/tmp`: 292637003776 available bytes; 83.67% used; 114209079 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106091548672 available bytes; 94.08% used; 114350527 free inodes.

server4 `/home`: 106091548672 available bytes; 94.08% used; 114350527 free inodes.

server4 `/data`: 292913917952 available bytes; 95.95% used; 225414567 free inodes.

server4 `/tmp`: 106091548672 available bytes; 94.08% used; 114350527 free inodes.

server4 `/var/tmp`: 106091548672 available bytes; 94.08% used; 114350527 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
