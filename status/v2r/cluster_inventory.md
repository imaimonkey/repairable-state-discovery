# V2R cluster inventory

2026-09-24T10:28:09.481046+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324411482112 available bytes; 81.90% used; 112489278 free inodes.

server1 `/home`: 324411482112 available bytes; 81.90% used; 112489278 free inodes.

server1 `/tmp`: 324411482112 available bytes; 81.90% used; 112489278 free inodes.

server1 `/var/tmp`: 324411482112 available bytes; 81.90% used; 112489278 free inodes.

server1 `/mnt/raid5`: 500167782400 available bytes; 97.71% used; 337698062 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57735471104 available bytes; 96.78% used; 110430671 free inodes.

server2 `/home`: 57735471104 available bytes; 96.78% used; 110430671 free inodes.

server2 `/tmp`: 57735471104 available bytes; 96.78% used; 110430671 free inodes.

server2 `/var/tmp`: 57735471104 available bytes; 96.78% used; 110430671 free inodes.

server2 `/mnt/raid5`: 512789364736 available bytes; 96.46% used; 445175421 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85366325248 available bytes; 95.24% used; 114173301 free inodes.

server3 `/home`: 85366325248 available bytes; 95.24% used; 114173301 free inodes.

server3 `/data`: 164322394112 available bytes; 97.73% used; 225818669 free inodes.

server3 `/tmp`: 85366325248 available bytes; 95.24% used; 114173301 free inodes.

server3 `/var/tmp`: 85366325248 available bytes; 95.24% used; 114173301 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105744629760 available bytes; 94.10% used; 114348968 free inodes.

server4 `/home`: 105744629760 available bytes; 94.10% used; 114348968 free inodes.

server4 `/data`: 153472872448 available bytes; 97.88% used; 225258405 free inodes.

server4 `/tmp`: 105744629760 available bytes; 94.10% used; 114348968 free inodes.

server4 `/var/tmp`: 105744629760 available bytes; 94.10% used; 114348968 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
