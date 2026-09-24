# V2R cluster inventory

2026-09-24T02:20:31.135810+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325396344832 available bytes; 81.85% used; 112498983 free inodes.

server1 `/home`: 325396344832 available bytes; 81.85% used; 112498983 free inodes.

server1 `/tmp`: 325396344832 available bytes; 81.85% used; 112498983 free inodes.

server1 `/var/tmp`: 325396344832 available bytes; 81.85% used; 112498983 free inodes.

server1 `/mnt/raid5`: 688197378048 available bytes; 96.84% used; 337733249 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40901681152 available bytes; 97.72% used; 110431608 free inodes.

server2 `/home`: 40901681152 available bytes; 97.72% used; 110431608 free inodes.

server2 `/tmp`: 40901681152 available bytes; 97.72% used; 110431608 free inodes.

server2 `/var/tmp`: 40901681152 available bytes; 97.72% used; 110431608 free inodes.

server2 `/mnt/raid5`: 529305317376 available bytes; 96.34% used; 445199644 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292225871872 available bytes; 83.69% used; 114186139 free inodes.

server3 `/home`: 292225871872 available bytes; 83.69% used; 114186139 free inodes.

server3 `/data`: 39771480064 available bytes; 99.45% used; 225847003 free inodes.

server3 `/tmp`: 292225871872 available bytes; 83.69% used; 114186139 free inodes.

server3 `/var/tmp`: 292225871872 available bytes; 83.69% used; 114186139 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106012536832 available bytes; 94.08% used; 114349853 free inodes.

server4 `/home`: 106012536832 available bytes; 94.08% used; 114349853 free inodes.

server4 `/data`: 289737424896 available bytes; 96.00% used; 225387695 free inodes.

server4 `/tmp`: 106012536832 available bytes; 94.08% used; 114349853 free inodes.

server4 `/var/tmp`: 106012536832 available bytes; 94.08% used; 114349853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
