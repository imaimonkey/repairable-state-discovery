# V2R cluster inventory

2026-09-24T02:18:57.831994+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325400522752 available bytes; 81.85% used; 112498977 free inodes.

server1 `/home`: 325400522752 available bytes; 81.85% used; 112498977 free inodes.

server1 `/tmp`: 325400522752 available bytes; 81.85% used; 112498977 free inodes.

server1 `/var/tmp`: 325400522752 available bytes; 81.85% used; 112498977 free inodes.

server1 `/mnt/raid5`: 694876598272 available bytes; 96.81% used; 337733298 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40903131136 available bytes; 97.72% used; 110431618 free inodes.

server2 `/home`: 40903131136 available bytes; 97.72% used; 110431618 free inodes.

server2 `/tmp`: 40903131136 available bytes; 97.72% used; 110431618 free inodes.

server2 `/var/tmp`: 40903131136 available bytes; 97.72% used; 110431618 free inodes.

server2 `/mnt/raid5`: 529364140032 available bytes; 96.34% used; 445199740 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292272259072 available bytes; 83.69% used; 114186776 free inodes.

server3 `/home`: 292272259072 available bytes; 83.69% used; 114186776 free inodes.

server3 `/data`: 18119761920 available bytes; 99.75% used; 225847027 free inodes.

server3 `/tmp`: 292272259072 available bytes; 83.69% used; 114186776 free inodes.

server3 `/var/tmp`: 292272259072 available bytes; 83.69% used; 114186776 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106012590080 available bytes; 94.08% used; 114349853 free inodes.

server4 `/home`: 106012590080 available bytes; 94.08% used; 114349853 free inodes.

server4 `/data`: 289739165696 available bytes; 96.00% used; 225387727 free inodes.

server4 `/tmp`: 106012590080 available bytes; 94.08% used; 114349853 free inodes.

server4 `/var/tmp`: 106012590080 available bytes; 94.08% used; 114349853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
