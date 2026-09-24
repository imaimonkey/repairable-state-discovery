# V2R cluster inventory

2026-09-24T09:24:36.258427+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324461056000 available bytes; 81.90% used; 112489909 free inodes.

server1 `/home`: 324461056000 available bytes; 81.90% used; 112489909 free inodes.

server1 `/tmp`: 324461056000 available bytes; 81.90% used; 112489909 free inodes.

server1 `/var/tmp`: 324461056000 available bytes; 81.90% used; 112489909 free inodes.

server1 `/mnt/raid5`: 503179120640 available bytes; 97.69% used; 337714019 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57774575616 available bytes; 96.78% used; 110430830 free inodes.

server2 `/home`: 57774575616 available bytes; 96.78% used; 110430830 free inodes.

server2 `/tmp`: 57774575616 available bytes; 96.78% used; 110430830 free inodes.

server2 `/var/tmp`: 57774575616 available bytes; 96.78% used; 110430830 free inodes.

server2 `/mnt/raid5`: 496458084352 available bytes; 96.57% used; 445177745 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85854801920 available bytes; 95.21% used; 114198972 free inodes.

server3 `/home`: 85854801920 available bytes; 95.21% used; 114198972 free inodes.

server3 `/data`: 165838471168 available bytes; 97.71% used; 225820981 free inodes.

server3 `/tmp`: 85854801920 available bytes; 95.21% used; 114198972 free inodes.

server3 `/var/tmp`: 85854801920 available bytes; 95.21% used; 114198972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757970432 available bytes; 94.10% used; 114349051 free inodes.

server4 `/home`: 105757970432 available bytes; 94.10% used; 114349051 free inodes.

server4 `/data`: 205084442624 available bytes; 97.17% used; 225273299 free inodes.

server4 `/tmp`: 105757970432 available bytes; 94.10% used; 114349051 free inodes.

server4 `/var/tmp`: 105757970432 available bytes; 94.10% used; 114349051 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
