# V2R cluster inventory

2026-09-25T11:59:28.225407+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319047258112 available bytes; 82.20% used; 112478829 free inodes.

server1 `/home`: 319047258112 available bytes; 82.20% used; 112478829 free inodes.

server1 `/tmp`: 319047258112 available bytes; 82.20% used; 112478829 free inodes.

server1 `/var/tmp`: 319047258112 available bytes; 82.20% used; 112478829 free inodes.

server1 `/mnt/raid5`: 370920349696 available bytes; 98.30% used; 337549211 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22910861312 available bytes; 98.72% used; 110409974 free inodes.

server2 `/home`: 22910861312 available bytes; 98.72% used; 110409974 free inodes.

server2 `/tmp`: 22910861312 available bytes; 98.72% used; 110409974 free inodes.

server2 `/var/tmp`: 22910861312 available bytes; 98.72% used; 110409974 free inodes.

server2 `/mnt/raid5`: 326055100416 available bytes; 97.75% used; 445082060 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84214263808 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84214263808 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142122524672 available bytes; 98.04% used; 225812636 free inodes.

server3 `/tmp`: 84214263808 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84214263808 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105593806848 available bytes; 94.11% used; 114350234 free inodes.

server4 `/home`: 105593806848 available bytes; 94.11% used; 114350234 free inodes.

server4 `/data`: 232648265728 available bytes; 96.78% used; 224972881 free inodes.

server4 `/tmp`: 105593806848 available bytes; 94.11% used; 114350234 free inodes.

server4 `/var/tmp`: 105593806848 available bytes; 94.11% used; 114350234 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
