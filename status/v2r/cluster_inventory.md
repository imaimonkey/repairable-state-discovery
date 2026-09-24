# V2R cluster inventory

2026-09-24T08:47:13.342911+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324387053568 available bytes; 81.90% used; 112490288 free inodes.

server1 `/home`: 324387053568 available bytes; 81.90% used; 112490288 free inodes.

server1 `/tmp`: 324387053568 available bytes; 81.90% used; 112490288 free inodes.

server1 `/var/tmp`: 324387053568 available bytes; 81.90% used; 112490288 free inodes.

server1 `/mnt/raid5`: 504251682816 available bytes; 97.69% used; 337718495 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57798725632 available bytes; 96.78% used; 110430952 free inodes.

server2 `/home`: 57798725632 available bytes; 96.78% used; 110430952 free inodes.

server2 `/tmp`: 57798725632 available bytes; 96.78% used; 110430952 free inodes.

server2 `/var/tmp`: 57798725632 available bytes; 96.78% used; 110430952 free inodes.

server2 `/mnt/raid5`: 515622891520 available bytes; 96.44% used; 445179225 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85899530240 available bytes; 95.21% used; 114199583 free inodes.

server3 `/home`: 85899530240 available bytes; 95.21% used; 114199583 free inodes.

server3 `/data`: 173617184768 available bytes; 97.60% used; 225822169 free inodes.

server3 `/tmp`: 85899530240 available bytes; 95.21% used; 114199583 free inodes.

server3 `/var/tmp`: 85899530240 available bytes; 95.21% used; 114199583 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105768415232 available bytes; 94.10% used; 114349097 free inodes.

server4 `/home`: 105768415232 available bytes; 94.10% used; 114349097 free inodes.

server4 `/data`: 254547648512 available bytes; 96.48% used; 225273436 free inodes.

server4 `/tmp`: 105768415232 available bytes; 94.10% used; 114349097 free inodes.

server4 `/var/tmp`: 105768415232 available bytes; 94.10% used; 114349097 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
