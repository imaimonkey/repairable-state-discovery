# V2R cluster inventory

2026-09-24T02:21:12.349283+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325394362368 available bytes; 81.85% used; 112498969 free inodes.

server1 `/home`: 325394362368 available bytes; 81.85% used; 112498969 free inodes.

server1 `/tmp`: 325394362368 available bytes; 81.85% used; 112498969 free inodes.

server1 `/var/tmp`: 325394362368 available bytes; 81.85% used; 112498969 free inodes.

server1 `/mnt/raid5`: 685279645696 available bytes; 96.86% used; 337733313 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40895389696 available bytes; 97.72% used; 110431600 free inodes.

server2 `/home`: 40895389696 available bytes; 97.72% used; 110431600 free inodes.

server2 `/tmp`: 40895389696 available bytes; 97.72% used; 110431600 free inodes.

server2 `/var/tmp`: 40895389696 available bytes; 97.72% used; 110431600 free inodes.

server2 `/mnt/raid5`: 529304301568 available bytes; 96.34% used; 445200160 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292225273856 available bytes; 83.69% used; 114186139 free inodes.

server3 `/home`: 292225273856 available bytes; 83.69% used; 114186139 free inodes.

server3 `/data`: 39770247168 available bytes; 99.45% used; 225846968 free inodes.

server3 `/tmp`: 292225273856 available bytes; 83.69% used; 114186139 free inodes.

server3 `/var/tmp`: 292225273856 available bytes; 83.69% used; 114186139 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106012504064 available bytes; 94.08% used; 114349853 free inodes.

server4 `/home`: 106012504064 available bytes; 94.08% used; 114349853 free inodes.

server4 `/data`: 289739755520 available bytes; 96.00% used; 225387694 free inodes.

server4 `/tmp`: 106012504064 available bytes; 94.08% used; 114349853 free inodes.

server4 `/var/tmp`: 106012504064 available bytes; 94.08% used; 114349853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
