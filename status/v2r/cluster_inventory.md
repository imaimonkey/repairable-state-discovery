# V2R cluster inventory

2026-09-27T14:08:54.665756+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304748011520 available bytes; 83.00% used; 112401362 free inodes.

server1 `/home`: 304748011520 available bytes; 83.00% used; 112401362 free inodes.

server1 `/tmp`: 304748011520 available bytes; 83.00% used; 112401362 free inodes.

server1 `/var/tmp`: 304748011520 available bytes; 83.00% used; 112401362 free inodes.

server1 `/mnt/raid5`: 630265810944 available bytes; 97.11% used; 337424112 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13407342592 available bytes; 99.25% used; 110351810 free inodes.

server2 `/home`: 13407342592 available bytes; 99.25% used; 110351810 free inodes.

server2 `/tmp`: 13407342592 available bytes; 99.25% used; 110351810 free inodes.

server2 `/var/tmp`: 13407342592 available bytes; 99.25% used; 110351810 free inodes.

server2 `/mnt/raid5`: 526874927104 available bytes; 96.36% used; 444722960 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 78559408128 available bytes; 95.62% used; 114062776 free inodes.

server3 `/home`: 78559408128 available bytes; 95.62% used; 114062776 free inodes.

server3 `/data`: 1330658222080 available bytes; 81.61% used; 225757130 free inodes.

server3 `/tmp`: 78559408128 available bytes; 95.62% used; 114062776 free inodes.

server3 `/var/tmp`: 78559408128 available bytes; 95.62% used; 114062776 free inodes.
| server4 | True | ['0', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110996819968 available bytes; 93.81% used; 114372787 free inodes.

server4 `/home`: 110996819968 available bytes; 93.81% used; 114372787 free inodes.

server4 `/data`: 350772142080 available bytes; 95.15% used; 224727429 free inodes.

server4 `/tmp`: 110996819968 available bytes; 93.81% used; 114372787 free inodes.

server4 `/var/tmp`: 110996819968 available bytes; 93.81% used; 114372787 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
