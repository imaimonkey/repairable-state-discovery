# V2R cluster inventory

2026-09-25T11:16:39.819646+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319061254144 available bytes; 82.20% used; 112478867 free inodes.

server1 `/home`: 319061254144 available bytes; 82.20% used; 112478867 free inodes.

server1 `/tmp`: 319061254144 available bytes; 82.20% used; 112478867 free inodes.

server1 `/var/tmp`: 319061254144 available bytes; 82.20% used; 112478867 free inodes.

server1 `/mnt/raid5`: 365289107456 available bytes; 98.32% used; 337554568 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22907043840 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22907043840 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22907043840 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22907043840 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 328597893120 available bytes; 97.73% used; 445088331 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84139835392 available bytes; 95.30% used; 114155492 free inodes.

server3 `/home`: 84139835392 available bytes; 95.30% used; 114155492 free inodes.

server3 `/data`: 142083297280 available bytes; 98.04% used; 225814410 free inodes.

server3 `/tmp`: 84139835392 available bytes; 95.30% used; 114155492 free inodes.

server3 `/var/tmp`: 84139835392 available bytes; 95.30% used; 114155492 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105611976704 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105611976704 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238632820736 available bytes; 96.70% used; 224981726 free inodes.

server4 `/tmp`: 105611976704 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105611976704 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
