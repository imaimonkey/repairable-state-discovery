# V2R cluster inventory

2026-09-24T11:07:09.759558+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324372054016 available bytes; 81.90% used; 112488983 free inodes.

server1 `/home`: 324372054016 available bytes; 81.90% used; 112488983 free inodes.

server1 `/tmp`: 324372054016 available bytes; 81.90% used; 112488983 free inodes.

server1 `/var/tmp`: 324372054016 available bytes; 81.90% used; 112488983 free inodes.

server1 `/mnt/raid5`: 479339094016 available bytes; 97.80% used; 337692553 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 57693106176 available bytes; 96.78% used; 110430219 free inodes.

server2 `/home`: 57693106176 available bytes; 96.78% used; 110430219 free inodes.

server2 `/tmp`: 57693106176 available bytes; 96.78% used; 110430219 free inodes.

server2 `/var/tmp`: 57693106176 available bytes; 96.78% used; 110430219 free inodes.

server2 `/mnt/raid5`: 511620067328 available bytes; 96.46% used; 445174160 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85235142656 available bytes; 95.24% used; 114169064 free inodes.

server3 `/home`: 85235142656 available bytes; 95.24% used; 114169064 free inodes.

server3 `/data`: 163960709120 available bytes; 97.73% used; 225817108 free inodes.

server3 `/tmp`: 85235142656 available bytes; 95.24% used; 114169064 free inodes.

server3 `/var/tmp`: 85235142656 available bytes; 95.24% used; 114169064 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105733726208 available bytes; 94.10% used; 114348923 free inodes.

server4 `/home`: 105733726208 available bytes; 94.10% used; 114348923 free inodes.

server4 `/data`: 115728916480 available bytes; 98.40% used; 225258203 free inodes.

server4 `/tmp`: 105733726208 available bytes; 94.10% used; 114348923 free inodes.

server4 `/var/tmp`: 105733726208 available bytes; 94.10% used; 114348923 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
